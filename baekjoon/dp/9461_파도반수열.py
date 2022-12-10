def padovan(num):
    dp = [1, 1, 1, 2, 2]

    for index in range(5, num+1):
        dp.append(dp[index-1] + dp[index-5])

    return dp[num-1]

a = int(input())
for _ in range(a):
    print(padovan(int(input())))