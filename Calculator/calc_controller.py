import calc_io as io
import calc_processor as p
from datetime import datetime as dt
from time import time

def t():
    return dt.now().strftime('%D\t%H:%M:%S')


def calculate():
    io.write_log(t(), 'Начало работы')
    input_a = io.input_number(1)
    io.write_log(t(), f'Первое число - {input_a}')
    input_b = io.input_number(2)
    io.write_log(t(), f'Второе число - {input_b}')
    operation_key = io.menu('complex' in (
        type(input_a).__name__, type(input_b).__name__))

    match operation_key:
        case '1': f = p.summ
        case '2': f = p.sub
        case '3': f = p.mult
        case '4': f = p.div
        case '5': f = p.pow
        case '6': f = p.whole_div
        case '7': f = p.tile_div
        case _:
            io.write_log(t(), 'Завершение работы')
            exit()
    oper_chars = ('+', '-', '*', '/', '^', '//', '%')        
    calc = p.calc(f, input_a, input_b)
    io.write_console(input_a, oper_chars[int(
        operation_key)-1], input_b, ' = ', calc)
    io.write_log(t(), input_a, oper_chars[int(
        operation_key)-1], input_b, '\t=\t', calc)
    io.write_log(t(), 'Завершение работы')


if __name__ == '__main__':
    pass