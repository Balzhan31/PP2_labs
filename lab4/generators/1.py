"""Create a generator that generates the squares of numbers up to some number N."""
def gen_squares():
    x = int(input())
    for i in range(1, x + 1):
        yield i**2
print(*gen_squares())
        