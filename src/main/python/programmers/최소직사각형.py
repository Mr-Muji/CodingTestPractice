"""
최소직사각형
프로그래머스 Lv1 완전탐색
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""

# 삼항 연산자


def solution(sizes):
    answer = 0
    answer_list = [0, 0]
    for size in sizes:
        size = sorted(size)
        answer_list[0] = answer_list[0] if answer_list[0] >= size[0] else size[0]
        answer_list[1] = answer_list[1] if answer_list[1] >= size[1] else size[1]

    answer = answer_list[0] * answer_list[1]
    
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
