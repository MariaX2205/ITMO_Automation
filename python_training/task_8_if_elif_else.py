num_float = -20

if num_float > 0:
    print ('положительное число')
elif num_float == 0:
    print ('ноль')
else:
    print('число отрицательное')

num = 3
permit_print = False

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

x = 7

if x >= 1 and x <= 4:
    print('Бакалавр')
elif x <7:
    print ('Магистр')
elif x in range (7, 9):
    print('аспирант')
else:
    print(' Введите корректный год обучения')

a = 105
if a not in range (-100, 100):
    print('-')
else:
    print('+')

