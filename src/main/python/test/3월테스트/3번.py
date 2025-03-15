"""
3번 문제
https://kakao-tech-bootcamp.goorm.io/learn/lecture/55237/%ED%8C%90%EA%B5%90-2%EA%B8%B0-%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%85%8C%ED%81%AC-%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B0%95%EC%A2%8C/lesson/2547540/3%EB%B2%88

"""

import sys

input = sys.stdin.readline

K = int(input())

# K = 100

MOV_CNT = 0
move_to = []
answer = [210, 0, 0]


def hanoi(n, A, B, C):
    global MOV_CNT
    # n == 1 일때는 끝내기
    if n == 1:
        # 남은 하나를 A에서 C로
        # TODO
        # move_to.append([A, C])
        answer[A] -= n
        answer[C] += n
        MOV_CNT += 1
        if K == MOV_CNT:
            print(f"{answer[0]} {answer[1]} {answer[2]}")
        return
    # 1. n-1 개를 A에서 B로
    hanoi(n - 1, A, C, B)
    # 2. 남은 하나를 A에서 C로
    # TODO
    # move_to.append([A, C])
    # 옮기기
    answer[A] -= n
    answer[C] += n
    MOV_CNT += 1
    if K == MOV_CNT:
        print(f"{answer[0]} {answer[1]} {answer[2]}")
    # 3. B에 있는 n-1개를 C로
    hanoi(n - 1, B, A, C)


hanoi(20, 0, 1, 2)
