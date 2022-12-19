from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import processor as p

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# def get_cplx_keys():
#     # Генератор клавиатуры для комплексных чисел - на будущее
#     btn_sym = ['+', '1', '2', '3', 'j', '-', '4', '5', '6',
#                '(', '*', '7', '8', '9', ')', '/','**', '.', '0', '=', 'Del', 'C']
#     buttons = list(map(lambda x: types.InlineKeyboardButton(
#         text=x, callback_data=x), btn_sym))  # Колбэк кнопки совпадает с ее маркировкой+j
#     keyboard = types.InlineKeyboardMarkup(row_width=5)
#     keyboard.add(*buttons[:-2])
#     keyboard.add(buttons[-1], buttons[-2])
#     return keyboard

def get_keys():
    # Генератор клавиатуры.
    btn_sym = ['+', '1', '2', '3', '**', '-', '4', '5', '6',
               '//', '*', '7', '8', '9', '%', '/', '.', '0', '=', 'Del', 'C']
    buttons = list(map(lambda x: types.InlineKeyboardButton(
        text=x, callback_data=x), btn_sym))  # Колбэк кнопки совпадает с ее маркировкой
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    keyboard.add(*buttons[:-1])
    keyboard.add(buttons[-1])
    return keyboard


@dp.message_handler(commands=["help", "hello", "calc"])
async def cmd_numbers(message: types.Message):
    match message.text[1:]:
        case 'help':
            await message.reply(f'Привет, {message.from_user.first_name}!\n/hello - поздороваться\n/help - вывод списка команд\n/calc - запуск калькулятора\n', reply=False)
        case 'hello':
            await message.reply(f'Привет, {message.from_user.first_name}!', reply=False)
        case 'calc':
            await message.answer("0", reply_markup=get_keys())


async def update_text(message: types.Message, new_value: int):
    # Общая функция для обновления текста с отправкой той же клавиатуры
    await message.edit_text(f"{new_value}", reply_markup=get_keys())


@dp.callback_query_handler()
async def callbacks_num(call: types.CallbackQuery):
    if call.data == 'log':
        await call.answer()
        return
    cur_value = call.message.text
    action = call.data
    # обработка нажатия кнопок при уже посчитанном значении в строке вывода
    if cur_value.count('=') != 0:
        if action == 'C':
            out_val = '0'
        elif action == '.':
            out_val = cur_value[cur_value.index('=')+2:]+'.'
        elif action == '=':
            out_val = cur_value[cur_value.index('=')+2:]
        else:
            s = ' ' if action in p.sep else ''
            out_val = cur_value[cur_value.index('=')+2:]+s+action
        await update_text(call.message, out_val)
        await call.answer()
        return

    match action:
        case 'C':
            out_val = '0'
        case 'Del':
            out_val = cur_value[:-1] if len(cur_value) != 1 else '0'
        case '=':
            ps = p.prepare_string(cur_value)
            cs = p.calc_string(ps)
            out_val = ps + ' = '+cs if len(ps.split()) > 1 else ps
            if cur_value != out_val:
                p.write_log(p.t(), f'Вычисление: {out_val}')
        case s if s in p.sep:   #'+' | '-' | '*' | '**' | '/' | '%' | '//':
            if cur_value == '0':
                out_val = '' if action == '-' else '0'
            else:
                out_val = cur_value+' '+action
        case '.':  # обработка второй точки в числе - не даем ставить если уже есть
            if cur_value == '0':
                out_val = '0.'
            else:
                if p.prepare_string(cur_value).split()[-1].count('.') == 0:
                    out_val = cur_value+action
                else:
                    out_val = cur_value
        case _:
            if cur_value[-1].isnumeric() or cur_value[-1] == '.':
                if cur_value == '0':
                    cur_value = ''
                out_val = cur_value + action
            else:
                out_val = cur_value + action if cur_value == '-' else cur_value + ' ' + action

    if out_val != cur_value: #если не поменялось - незачем и обновлять
        await update_text(call.message, out_val)
    # Не забываем отчитаться о получении колбэка - чтобы "часики не висели"
    await call.answer()

if __name__ == '__main__':
    try:
        p.write_log(p.t(), 'Старт сервера - начало работы бота')
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        p.write_log(p.t(), 'Остановка сервера - завершение работы бота')        