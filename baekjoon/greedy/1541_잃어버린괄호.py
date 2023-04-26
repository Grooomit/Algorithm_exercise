import sys
input = sys.stdin.readline

num = input()

def solution(num):
    result = 0
    nums = num.split('-')

    for i in range(len(nums)):
        i_num = [int(x) for x in nums[i].split('+')]
        if i == 0:
            result += sum(i_num)
        else:
            result -= sum(i_num)
    
    return result

print(solution(num))