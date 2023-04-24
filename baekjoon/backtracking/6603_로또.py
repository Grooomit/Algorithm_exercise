'''
1. 아이디어
- N 개줄 입력, 0입력시 exit
- 각 줄에서 0번 인덱스를 제외한 리스트를 조합으로 돌린다.
- print(조합인덱스값)

2. 시간복잡도
- +for 문 : O(총 케이스 수)
- *조합 13C6 = 1716

3. 자료구조
- 조합리스트 comb : int[]
'''

from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    N = list(map(int, input().split()))
    
    if N[0] == 0:
        break

    S = N[1:]
    combs = combinations(S, 6)
    for comb in combs:
        print(*comb, sep=' ')
    
    print()