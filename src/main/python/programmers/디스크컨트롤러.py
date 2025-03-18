"""
디스크 컨트롤러
프로그래머스 Lv3
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""

import heapq
from collections import deque


def solution(jobs):
    answer = 0
    time = 0
    total_time = 0
    jobs_len = len(jobs)
    jobs.sort()

    wait_queue = []

    # 처리 시간이 앞에 오도록 변경.
    for job in jobs:
        temp = job[0]
        job[0] = job[1]
        job[1] = temp

    # 잡을 큐로 만들어준다. 그래줄 필요가 있나?
    jobs_queue = deque()
    for job in jobs:
        jobs_queue.append(job)
    
    # print(jobs_queue[0][1])

    # for job in jobs:

    while jobs_queue or wait_queue:  # 큐가 빌때까지 반복
    
        while jobs_queue and jobs_queue[0][1] <= time:  # 시간이 맞게 걸리면 다 빼낸다
            heapq.heappush(wait_queue, jobs_queue.popleft())    # 시간이 됐으면 잡큐에서 빼서 대기큐(힙)에 힙푸시 해준다.

        if wait_queue:
            i = heapq.heappop(wait_queue)
            # in_work = 1
            
            total_time += (time - i[1] + i[0])
            time += i[0]
        else:
            time = jobs_queue[0][1]

    answer = total_time // jobs_len
    return answer


print(solution([[0, 3], [1, 9], [3, 5]]))
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]))
