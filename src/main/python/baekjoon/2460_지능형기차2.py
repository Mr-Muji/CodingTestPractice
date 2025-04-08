"""
지능형기차2

난이도: 브론즈 2

https://www.acmicpc.net/problem/2460
"""

import sys

input = sys.stdin.readline


def solution():
    current = 0
    max = 0
    people_off = 0
    people_on = 0

    for _ in range(10):
        people_off, people_on = map(int, input().split())
        current = current - people_off + people_on
        if max < current:
            max = current

    print(max)


solution()
