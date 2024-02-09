def palindrom(s):
    t = s[::-1]
    if t == s:
        print('Yes')
    else:
        print('No')

palindrom(input())