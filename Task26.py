# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

listPositive = []
n = int(input('Введите целое число: '))
nX = n
n1, n2 = 0, 1
if nX == 0:
    listPositive.append(n1)
else:
    for i in range(nX+1):
        listPositive.append(n1)
        nX = n1 + n2
        n1 = n2
        n2 = nX
print(listPositive)



