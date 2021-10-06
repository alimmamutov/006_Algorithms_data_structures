# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
bigList = []
print('Введите пожалуйста матрицу 4 * 4 построчно через пробел (только целые)')
for number in range(1, 5):
    while True:
        try:
            myStr = input(f'Введите {number}-ю строку матрицы: ')
            myList = [int(i) for i in myStr.split()]
            if len(myList) == 4:
                myList.append(sum(myList))
                bigList.append(myList)
                break
            else:
                raise ValueError
        except ValueError:
            print('Неправильный ввод!')
            continue
for item in bigList:
    print(item)
