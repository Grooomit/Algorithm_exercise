def tile(num):
    if num <= 1:
        return num
    a, b = 1, 2

    for i in range(3, num+1):
        a, b = b, a+b

    return b

a = int(input())
print(tile(a) % 10007)