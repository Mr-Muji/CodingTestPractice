"""
프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
자바로도 풀었었음. 이 레포 안에 있음.
/
"""


def solution(priorities, location):
    from collections import deque
    answer = 0
    # {처음 순서(ABCD), 우선순위} 형식으로 큐에 넣기
    process_queue = deque()
    for i, prio in enumerate(priorities):
        process_queue.append({i + 1, prio})

    print(process_queue)

    # priorities를 역순으로 정렬해서 큐에 넣기
    # prio queue 에서 팝해서, 순서큐에서 우선순위가 같은게 나올때까지 팝


    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
