def square():
    x = int(input())
    y = int(input())
    for i in range(x, y + 1):
        yield i ** 2
        
for i in square():
    print(i)