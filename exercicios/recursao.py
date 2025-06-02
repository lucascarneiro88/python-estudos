def fatorial(n):
    """Cálculo do fatorial de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def fib(n):
    """Número de Fibonacci recursivo."""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(f'Fatorial de 5: {fatorial(5)}')
    print(f'Fibonacci de 5: {fib(5)}')
