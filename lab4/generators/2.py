"""Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console."""
def even():
    x = int(input())
    for i in range(0, x + 1):
        if i == x and i % 2 == 0:
            yield i
        elif i % 2 == 0:
            yield i
            if i < x - 1:
                yield ','
print(*even())
