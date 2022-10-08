# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listOne = [1.1, 1.2, 3.1, 5, 10.01]
listTwo = []
for i in range(len(listOne)):
    listOne[i] = listOne[i] - round(listOne[i])
    listTwo.append(round((listOne[i]), 2))
print(listTwo)

maxValue = listTwo[i]
minValue = listTwo[i]
for i in range(len(listTwo)):
    if listTwo[i] > maxValue:
        maxValue = listTwo[i]
    if listTwo[i] < minValue and listTwo[i] > 0:
        minValue = listTwo[i]
print(f'Разница между максимальным и минимальным значением дробной части:\n{maxValue} - {minValue} = {maxValue-minValue}')

