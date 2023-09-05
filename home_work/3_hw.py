# 2
def task_2():
    x = 7
    y = 5

    return max(x, y)


print(task_2())


# 3
def task_3():
    x = 135
    y = 100

    if x - y == 135 or y - x == 135:
        print('yes')
    else:
        print('No')


task_3()


# 4
def task_4():
    s = 5

    if s == 12:
        print('Winter')
    if s in range(1, 3):
        print('Winter')
    elif s in range(3, 6):
        print('Spring')
    elif s in range(6, 9):
        print('Summer')
    elif s in range(9, 12):
        print('Autumn')
    else:
        print('Please enter the number from 1 to 12')


task_4()


# 5
def task_5():
    x = 2
    y = 30
    z = 40
    if x > 10 and y > 10 and z > 10:
        print('Yes')
    else:
        print('No')


task_5()


# 6
def task_6():
    l = [1, 2, -3, -4, 9]
    pos_count = 0
    for num in l:
        if num >= 0:
            pos_count += 1
    print("Количество положительных чисел - ", pos_count)


task_6()


# 7
def task_7():
    a = 4
    b = 0
    days = ((b * 29) + (a * 29 * 12))
    print('Количество дней - ', days)


task_7()
