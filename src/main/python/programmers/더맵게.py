"""
더 맵게
프로그래머스 Lv 2 힙
https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""

import heapq


def solution(scoville, K):
    answer = 0
    cnt = 0
    a, b, c = 0, 0, 0

    heapq.heapify(scoville)

    for _ in range(len(scoville) - 1):
        if scoville[0] >= K:
            break
        cnt += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + b * 2
        heapq.heappush(scoville, c)  # O(n)

    if c < K and c != 0:
        return -1

    answer = cnt
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1], 1))
