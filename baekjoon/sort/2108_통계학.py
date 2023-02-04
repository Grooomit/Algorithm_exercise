'''
1. 아이디어
- N 개의 값을 받아서 평균, 중앙값, 최빈값, 범위를 출력한다.

2. 시간복잡도

3. 자료구조
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

def freq(list):
    cnt_dict = {}
    for i in list:
        if i in cnt_dict:
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 1
    
    max_value = max(cnt_dict.values())
    
    mode = [k for k,v in cnt_dict.items() if v == max_value]

    if len(mode) > 1:
        return sorted(mode)[1]
    
    return mode[0]


def ran(list):
    return max(list) - min(list)

def middle(list):
    list.sort()
    return list[len(list)//2]

def aver(list):
    return round(sum(list) / len(list), 1)

print(aver(nums))
print(middle(nums))
print(freq(nums))
print(ran(nums))
