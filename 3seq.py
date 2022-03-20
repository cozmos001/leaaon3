'''
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
'''
# Вариант с любыми элементами и любым разделителем из предложенных - 1, Alex, 0.5/Poll;True
numbers_1 = input('Введите элементы 1-го списка через запятую, точку с запятой или слэш: ')
numbers_1 = list([i for i in numbers_1.replace(';', ',').replace('/', ',').split(',')])
numbers_2 = input('Введите элементы 2-го списка через запятую, точку с запятой или слэш: ')
numbers_2 = list([i for i in numbers_2.replace(';', ',').replace('/', ',').split(',')])
numbers_3 = list(set(numbers_1) - set(numbers_2))
print('Результат:', ', '.join(str(i) for i in numbers_3))

# Вариант только с цифрами - 1,2,3,4,5
numbers_1 = input('Введите элементы 1-го списка через запятую, точку с запятой или слэш: ')
numbers_1 = list([int(i) for i in numbers_1.replace(';', ',').replace('/', ',').split(',')])
numbers_2 = input('Введите элементы 2-го списка через запятую, точку с запятой или слэш: ')
numbers_2 = list([int(i) for i in numbers_2.replace(';', ',').replace('/', ',').split(',')])
numbers_3 = list(set(numbers_1) - set(numbers_2))
print('Результат:', ', '.join(str(i) for i in numbers_3))
