"""
이진수

난이도: 브론즈 1

https://www.acmicpc.net/problem/3460

포인트
출력 방식: 공백으로 구분된 정수 목록을 어떻게 출력할 수 있을까?
    '*' 연산을 이용해 리스트를 분해해서 출력
    예시: print(*answer_list)

"""

def solution():
    import sys

    input = sys.stdin.readline

    T = int(input())
    list_n = []
    for _ in range(T):
        list_n.append(int(input()))
    
    # print(list_n)
    answer_list = []
    for i, n in enumerate(list_n):
        cnt = 20
        while cnt >= 0:
            if 2 ** (cnt + 1) > n >= 2**cnt:
                n -= 2**cnt
                answer_list.append(cnt)
            cnt -= 1
        answer_list.sort()
        print(*answer_list)
        answer_list.clear()
        

solution()
