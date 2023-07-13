'''
순열로 만들 수 있는 숫자 리스트를 만든다.
set 으로 중복 제거
소수인지 확인
'''

import math
from itertools import permutations

def solution(numbers):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**(1/2))+1):
            if (num % i) == 0:
                return False
        return True
    
    answer = 0
    arr = set()
    for i in range(1, len(numbers)+1):
    	arr |= set(map(int, map(''.join, permutations(list(numbers), i))))
    
    for i in arr:
        if isPrime(i):
            answer += 1
            
    return answer