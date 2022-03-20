'''
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
'''
count = int(input('Введите кол-во элементов: '))
lst = []
for i in range(1, count + 1):
    digit = int(input(f'Введите {i} элемент: '))
    lst.append(digit)
lst.sort()
print('Вывод:', lst)
