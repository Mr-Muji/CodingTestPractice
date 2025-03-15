"""
250315
하노이의 탑
프로그래머스 Lv2
https://school.programmers.co.kr/learn/courses/30/lessons/12946?language=python3

"""


def solution(n):
    hanoi(n, 1, 2, 3)
    return answer


answer = []


def hanoi(n, A, B, C):
    if n == 1:
        answer.append([A, C])
        return

    # 1. n-1개의 원반을 A 에서 B로 옮김

    hanoi(n - 1, A, C, B)

    # 2. 남은 한 개의 원반을 A에서 C로 옮김
    answer.append([A, C])

    # 3. B에 있는 n-1 개의 원반을 C로 옮김
    hanoi(n - 1, B, A, C)


print(solution(2))
