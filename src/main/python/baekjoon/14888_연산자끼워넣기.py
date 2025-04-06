"""
14888_연산자끼워넣기
링크: https://www.acmicpc.net/problem/14888
"""


def solution():
    import sys

    input = sys.stdin.readline

    sys.setrecursionlimit(10**6)

    N = int(input())

    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    max_result = -int(1e9)
    min_result = int(1e9)

    def dfs(index, current, plus, minus, mul, div):
        nonlocal max_result, min_result

        if index == N:
            max_result = max(max_result, current)
            min_result = min(min_result, current)

        if plus:
            dfs(index + 1, current + numbers[index], plus - 1, minus, mul, div)
        if minus:
            dfs(index + 1, current - numbers[index], plus, minus - 1, mul, div)
        if mul:
            dfs(index + 1, current * numbers[index], plus, minus, mul - 1, div)
        if div:
            dfs(index + 1, current // numbers[index], plus - 1, minus, mul, div)

    dfs(1, numbers[0], *operators)
