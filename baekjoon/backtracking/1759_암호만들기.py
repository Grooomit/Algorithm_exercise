'''
1. 아이디어
* 암호 : 최소 한개의 모음과 최소 두개의 자음으로 구성
* 암호는 알파벳 순으로 정렬
- 주어진 알파벳을 정렬한다.
- 백트래킹으로 L 개의 알파벳을 뽑는다. (조합)
- 뽑은 알파벳에 "최소 1개의 모음, 최소 2개의 자음" 이 존재하는지 확인
- 뽑은 알파벳 출력

2. 시간복잡도
* (3 ≤ L ≤ C ≤ 15)
- 백트래킹 : 15C7 = 6435
- 정렬 : O(C log C)
- 조건확인 : O(1) - set() 을 이용한 해시탐색

3. 자료구조
- 알파벳 모음 alphabet : str[]
'''

from itertools import  combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = sorted(input().split())
sset = set(['a', 'e', 'i', 'o', 'u'])

def backtracking(word, num, vowel):
    if len(word) == L:
        if vowel > 0 and len(word) - vowel >= 2: 
            print("".join(word))
        return
    
    for i in range(num, len(alphabet)):
        if alphabet[i] in sset:
            vowel += 1
        word.append(alphabet[i])
        backtracking(word, i+1, vowel)
        if alphabet[i] in sset:
            vowel -= 1
        word.pop()

backtracking([], 0, 0)