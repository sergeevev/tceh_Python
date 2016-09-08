input('Ответь на несколько вопросов. Если готов, нажми Enter.')

correct = 0


q1 = input('Какой язык мы изучаем?')
if q1 == 'python' or 'Python':
    correct += 1
    print('Верно')
elif:
    print('Ты точно был на занятии?')

q2 = input('25 это int или float?')
if q2 == 'int':
    correct += 1
    print('Верно')
elif:
    print('Не угадал...')

q3 = input('Все в Python?')
if q3 == 'Объект' or 'Object':
    correct += 1
    print('Верно')
elif:
    print('Неа')

q4 = input('"Неопределенная" константа в Python присваевается значением ...')
if q4 == 'None' or 'none':
    correct += 1
    print('Верно')
elif:
    print(' Прости, но нет')

q5 = input('В какой кодировке символ из ASCII занимает 1 байт?')
if q5 == 'UTF-8':
    correct += 1
    print('Верно')
elif:
    print('Ты точно был на занятии?')

print('На этом все. Ты ответил верно на %d вопросов! \nУдачи!' %(correct))