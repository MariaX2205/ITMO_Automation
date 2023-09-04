a: int = 5
b: str = 'string'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))

def str_length(s='') -> int:
    return len(s)
print(2)

def list_length(l1: list, l2: list) -> int:
    return max(len(l1), len(l2))

print(max(12, 23))