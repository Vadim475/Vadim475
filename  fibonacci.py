class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def fibonacci_sum(limit):
    total_sum = 0
    fib_iter = FibonacciIterator()

    while True:
        fib_num = next(fib_iter)
        if fib_num >= limit:
            break
        if fib_num % 2 == 0:
            total_sum += fib_num

    return total_sum

limit = 4000000


result = fibonacci_sum(limit)
print(limit, "is:", result)

