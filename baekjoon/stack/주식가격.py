'''
1. 아이디어
> 각 인덱스의 값보다 작은 수가 나타날때까지 걸리는 시간 구하기
- for 문으로 주어진 prices 를 순회한다. O(N)
  - 각 인덱스들을 for 문 한번만에 처리할 수 있는 방법은 없나?
- stack 에 인덱스를 담는다.
  - 최근에 담은 stack 의 값이 현재 index의 값보다 크다면 stack.pop()
  - 아니라면 반복
- for 문을 전부 순회한 후 남은 stack 값은 len(prices) - index - 1

2. 시간복잡도
- for문 : O(N)

3. 자료구조

'''
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, value in enumerate(prices):
        while stack and stack[-1][1] > value:
            idx, _ = stack.pop()
            answer[idx] = i - idx
        
        stack.append((i, value))
        
    for i, v in stack:
        answer[i] = len(prices) - 1 - i
        
    return answer