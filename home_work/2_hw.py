def task_1(a: int, b: float, c: str, d: list, e: bool) -> list:
    a = 1
    b = 5.5
    c = "string"
    d = [1, 2, 3]
    e = True
    print(" а : ", type(a), "\n", "b : ", type(b), "\n", "c : ", type(c),
          "\n", "d : ", type(d), "\n", "e : ", type(e))

    return


task_1(1, 5.5, 'string', [1, 2, 3], 'True')


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(task_2(), " - this is the part of Fibonacci sequence.")


def task_3(x: int) -> int:
    return x ** 2


print(task_3(55))


