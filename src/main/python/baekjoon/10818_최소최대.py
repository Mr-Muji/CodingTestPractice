def solution():
    import sys

    input = sys.stdin.readline

    N = int(input())
    nums = list(map(int, input().split()))

    max_num = max(nums)
    min_num = min(nums)

    print(min_num, max_num)


solution()
