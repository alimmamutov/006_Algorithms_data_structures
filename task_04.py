# 4. Определить, какое число в массиве встречается чаще всего.

import random

r = [random.randint(0, 100) for _ in range(100)]

print(f'Массив {r}')

rNew = [r.count(i) for i in r]
maxCount = max(rNew)
rNew = list(zip(rNew, r))

r = []
for i in rNew:
    if i[0] == maxCount:
        r.append(i[1])

print(f'Самыое часто встречающееся число: {set(r)}')
