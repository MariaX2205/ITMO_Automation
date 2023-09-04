# определяем функцию
def add(x, y):
    return x + y


# вызываем функцию
print(add(1, 2))

# вызывем функцию с другими аргументами
print(add('I a', 'm a tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))

print(arg(2, 2))

#print(arg(2, 2, '1', 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


def main(a=(1, 2, 3, 4)):
    return [1]

print(main())


def arg_2(r, p=3.14159):
    S = p * r ** 2
    return S


print(arg_2(3))
