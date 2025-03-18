"""
프로세스
스택/큐
프로그래머스 Lv2
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""

from collections import deque


def solution(priorities, location):
    answer = 0

    q = deque()
    for i, priority in enumerate(priorities):
        q.append([priority, i])

    # priorities.sort(reverse=True)

    cnt = 0
    while q:
        
        process = q.popleft()
        priority = process[0]
        if max(priorities) == priority:
            cnt += 1
            priorities.remove(priority)
            if process[1] == location:
                answer = cnt
                break
        else:
            q.append(process)

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
