input('Ответь на несколько вопросов. Если готов, нажми Enter.')

correct = 0


q1 = input('Какой язык мы изучаем?')
if q1 == 'python' or 'Python':
    correct += 1
    print('Верно')
elif:
    print('Ты точно был на занятии?')

q1 = input('25 это int или float?')
if q1 == 'int':
    correct += 1
    print('Верно')
elif:
    print('Не угадал...')

q1 = input('Все в Python?')
if q1 == 'Объект' or 'Object':
    correct += 1
    print('Верно')
elif:
    print('Неа')

q1 = input('"Неопределенная" константа в Python присваевается значением ...')
if q1 == 'None' or 'none':
    correct += 1
    print('Верно')
elif:
    print(' Прости, но нет')

q1 = input('В какой кодировке символ из ASCII занимает 1 байт?')
if q1 == 'UTF-8':
    correct += 1
    print('Верно')
elif:
    print('Ты точно был на занятии?')

print('На этом все. Ты ответил верно на %d вопросов! \nУдачи!' %(correct))