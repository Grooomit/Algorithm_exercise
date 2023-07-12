'''
1. 아이디어
- 100 번 채널에서 +, - 로 채널을 이동하는 경우
- 숫자 버튼을 이용하여 가장 가까운 채널을 이동 후 +, - 로 채널을 이동하는 경우
=> 두 경우를 계산하여 더 작은 값을 출력
  
2. 시간복잡도
- for 문 : O(N)

3. 자료구조

'''

import sys
input = sys.stdin.readline

def solution():
    # 고장난 버튼 체크
    def check(num):
        num = list(str(num))
        for i in num:
            if i in broken:
                return False
        return True
    
    channel = int(input())
    N = int(input())
    broken = list(input().split())

    # 숫자를 누르지 않고 +, -로 이동하는 경우
    min_cnt = abs(channel - 100)

    # 숫자 버튼을 이용하여 가장 가까운 채널로 이동 후 +, -로 이동하는 경우
    for i in range(1000001):
        if check(i):
            # 숫자를 누르지 않고 이동한 경우와 비교하여 더 작은 값을 적용
            min_cnt = min(min_cnt, len(str(i)) + abs(i - channel))

    print(min_cnt)

solution()