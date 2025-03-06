"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
스택
"""


def solution(arr):
    from collections import deque
    answer = []
    queue = deque()

    for i in arr:
        queue.append(i)

    n = -1
    while queue:
        curr_num = queue.popleft()
        if n != curr_num:
            answer.append(curr_num)
        n = curr_num

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
#print(solution([4, 4, 4, 3, 3]))
