# Создайте функцию генератор чисел Фибоначчи

def generate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


fib_gen = generate_fibonacci(20)
for i in fib_gen:
    print(i)
