# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if not(w and z or not y or not x == (not w)):
                    print (w, z, y, x)