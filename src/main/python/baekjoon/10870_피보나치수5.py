"""
피보나치 수 5

난이도: 브론즈 2

https://www.acmicpc.net/problem/10870

"""

import sys
input = sys.stdin.readline

def solution():
    n = int(input())

    p_1 = 0
    p_2 = 1
    result = 0
    for _ in range(n):
        result = p_1 + p_2
        p_1 = p_2
        p_2 = result

    print(p_1)

solution()

