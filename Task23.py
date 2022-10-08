# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
listOne = [2, 3, 4, 5, 6]
listTwo = []
for i in range(0, math.ceil(len(listOne)/2)):
    new_element = listOne[i] * listOne[len(listOne)-1-i]
    listTwo.append(new_element)
print(listTwo)