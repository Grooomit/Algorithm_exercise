def isPalindrome(data):
    return recursion(data, 0)

def recursion(data, l):
    if len(data) <= 1:
        return 1, l+1
    elif data[0] != data[-1]:
        return 0, l+1
    else:
        return recursion(data[1:-1], l+1)


n = int(input())
for i in range(n):
    data = isPalindrome(input())
    print(data[0], data[1], sep=" ")
