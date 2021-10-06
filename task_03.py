# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

r = [random.randint(0, 99) for _ in range(20)]

print(f'Массив до замены {r}')

maxItem = max(r)
minItem = min(r)
minList, maxList = [], []
for i, item in enumerate(r):
    if item == maxItem:
        maxList.append(i)
    elif item == minItem:
        minList.append(i)

print(f'min: {minItem}, max {maxItem}')

for i in minList:
    r[i] = maxItem

for i in maxList:
    r[i] = minItem

print(f'Массив после замены {r}')
