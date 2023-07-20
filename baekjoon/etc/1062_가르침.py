'''
1. 아이디어
- 주어진 단어들을 set(list()) 로 변경한다.
- 단어길이가 짧은 순으로 알파벳 학습
- 학습한 알파벳을 set에 저장
- 단어와 학습한 알파벳 사이의 차가 적은 순으로 학습

2. 시간복잡도


3. 자료구조
- 학습한 알파벳 alphabet : str[]
- 읽을 수 있는 단어갯수 result : int
'''

from itertools import combinations
import sys
input = sys.stdin.readline

def solution(K, words):
    if K < 5: return 0
    if K == 26: return len(words)
    
    result = 0
    learn = {'a', 't', 'i', 'c', 'n'}
    not_learn = set(chr(i) for i in range(ord('a'), ord('z') + 1)) - learn

    words = [set(word) - learn for word in words]

    for comb in combinations(not_learn, K - 5):
        comb = set(comb)
        result = max(result, sum(1 for word in words if len(word - comb) == 0))

    return result

N, K = map(int, input().split())
words = [set(list(input().strip())) for _ in range(N)]
print(solution(K, words))