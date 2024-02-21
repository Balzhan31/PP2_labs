"""Implement a generator that returns all numbers from (n) down to 0."""
def numbers():
    x = int(input())
    for i in range(x, 0-1, -1):
        yield i
print(*numbers())