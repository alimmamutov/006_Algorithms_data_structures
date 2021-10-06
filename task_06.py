# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

r = [random.randint(1, 100) for i in range(15)]

print(f'Массив {r}')

maxItem, minItem = -1, 101
maxInd, minInd = 0, 0
for ind, item in enumerate(r):
    if maxItem < item:
        maxItem = item
        maxInd = ind
    if minItem > item:
        minItem = item
        minInd = ind

if maxInd < minInd:
    r = r[maxInd+1: minInd]
else:
    r = r[minInd+1: maxInd]
print(r)
print(f'Сумма {sum(r)}')


