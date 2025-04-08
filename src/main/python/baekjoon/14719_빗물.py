"""
빗물

난이도: 골드 5

https://www.acmicpc.net/problem/14719
"""

import sys

input = sys.stdin.readline


def solution():
    H, W = map(int, input().split())
    print(H)
    print(W)

    list_block = list(map(int, input().split()))

    print(list_block)

    top = 0
    sum = 0
    sum_temp = 0
    for i, height in enumerate(list_block):
        if top == 0 and top < height:
            top = height
            continue
        else:
            sum_temp += top - height

        if top != 0 and 
        
        


solution()
