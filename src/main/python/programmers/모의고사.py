"""
모의고사
프로그래머스 Lv1 완전탐색
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""


def solution(answers):
    answer = []
    score = [0, 0, 0]
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answers):
        if ans == man1[i % len(man1)]:
            score[0] += 1
        if ans == man2[i % len(man2)]:
            score[1] += 1
        if ans == man3[i % len(man3)]:
            score[2] += 1

    max_score = max(score)

    result = []
    for i, s in enumerate(score):
        if max_score == s:
            result.append(i + 1)
    answer = result
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
