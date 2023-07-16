'''
1. 아이디어
- stack 을 이용하여 주어진 괄호를 for문으로 순회한다.
- while 최근 stack 값과 현재 index 를 비교
    - [ 나 ( 이면 (depth, value) 형태로 stack 에 저장
    - ] 나 ) 이면 상위 depth 값을 전부 계산
        - depth list 를 만들고 현재 depth 계산할 때 상위 depth 값을 전부 곱한다.
        - 계산한 depth 값은 0으로 변경
- for 문 종료 후 while 문으로 stack_size != 0 이면 return 0

2. 시간복잡도
- for 문 : O(N)

3. 자료구조
- depth list dep: int[]
- stack: (int, int)[]
'''

string = input()
dep_sum = [0] * 30
stack = []
depth = 0

for v in string:
    if stack and ((v == ')' and stack[-1][1] == '(') or (v == ']' and stack[-1][1] == '[')):
        dep, _ = stack.pop()

        if v == ')':
            dep_sum[dep] += max(1, dep_sum[dep+1]) * 2
        else:
            dep_sum[dep] += max(1, dep_sum[dep+1]) * 3
        
        dep_sum[dep+1], depth = 0, depth-1
        continue
    
    stack.append((depth, v))
    depth += 1

if len(stack) != 0:
    print(0)
else:
    print(dep_sum[0])