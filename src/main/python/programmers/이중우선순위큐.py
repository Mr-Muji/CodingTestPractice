"""
이중우선순위큐
프로그래머스 Lv3
https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""

import heapq


def solution(operations):
    answer = []
    hq = []
    for op in operations:
        a, b = op.split()
        b = int(b)
        
        if a == "I":
            hq.append(b)
        elif a == "D":
            if hq:
                if b == -1:
                    heapq.heapify(hq)
                    heapq.heappop(hq)
                else:
                    hq = [-x for x in hq]
                    heapq.heapify(hq)
                    heapq.heappop(hq)
                    hq = [-x for x in hq]

    if hq:
        heapq.heapify(hq)
        a = heapq.heappop(hq)

        if not hq:  # 원소가 하나만 있었을 경우
            answer = [a, a]
        else:
            hq = [-x for x in hq]
            heapq.heapify(hq)
            b = -heapq.heappop(hq)
            answer = [b, a]
    else:
        return [0, 0]

    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)
