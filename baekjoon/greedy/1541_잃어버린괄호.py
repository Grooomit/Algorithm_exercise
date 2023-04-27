import sys
input = sys.stdin.readline

nums = input().split('-')

def solution(nums):
    result = sum(map(int, nums[0].split('+')))

    for i in range(1, len(nums)):
        result -= sum(map(int, nums[i].split('+')))
    
    return result

print(solution(nums))