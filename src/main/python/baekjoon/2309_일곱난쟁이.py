"""
일곱난쟁이

난이도: 브론즈 1

https://www.acmicpc.net/problem/2309

combination 함수 사용...
"""


import sys

from itertools import combinations

input = sys.stdin.readline


def solution():
    """
    조합 사용하여 풀기
    """
    list = []
    for _ in range(9):
        list.append(int(input()))

    for comb in combinations(list, 7):
        if sum(comb) == 100:
            for h in sorted(comb):
                print(h)
            break


def solution2():
    """
    조합 사용하지 않고 풀기
    """
    list = []
    for _ in range(9):
        list.append(int(input()))

    list.sort()

    for i in range(9):
        for j in range(i + 1, 9):
            if sum(list) - list[i] - list[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(list[k])


solution2()
