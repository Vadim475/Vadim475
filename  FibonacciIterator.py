class FibonacciIterator:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= 4000000:
            raise StopIteration
        else:
            self.prev, self.curr = self.curr, self.prev + self.curr
            return self.prev if self.prev % 2 == 0 else 0

if __name__ == "__main__":
    fib_iter = FibonacciIterator()
    even_sum = sum(fib_iter)
    print(even_sum)
