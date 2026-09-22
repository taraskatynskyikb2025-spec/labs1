def parne(n: int) -> bool:
    "Перевірка на парність testb"
    return n % 2 == 0
def factorial(n: int) -> int:
    "Обчислює факторіал n."
    if n <= 1:
        return 1
    return n * factorial(n - 1)