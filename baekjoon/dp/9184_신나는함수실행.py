def w(a, b, c):

    w = [[[]]]

    return 0



while(True):
    a, b, c = list(map(int, input().split()))
    if (a == b == c == -1):
        break

    print("w(a, b, c) = " + w(a, b, c))