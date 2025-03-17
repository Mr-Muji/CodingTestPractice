"""
다리를 지나는 트럭
프로그래머스 Lv2
https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    """
    거참까다롭네.
    """

    answer = 0
    bridge_queue = deque()
    # 초기 상태.
    for _ in range(bridge_length):
        bridge_queue.append(0)

    truck_queue = deque()
    for truck in truck_weights:
        truck_queue.append(truck)
    time = 0
    current_weight = 0

    while truck_queue:
        # bridge_stack 에서 leftpop
        current_weight -= bridge_queue.popleft()
        # time ++
        time += 1
        # truck_weight[0] 에다가 현재 다리 무게를 더해서 weight를 안넘으면 bridge_weight에 추가 (weight 를 안넘을 때만)
        if current_weight + truck_queue[0] <= weight:
            # 안넘으면 bridge_queue에도 추가.
            # truck_weights에서 leftpop
            truck = truck_queue.popleft()
            bridge_queue.append(truck)
            current_weight += truck

        # 넘으면 bridge_queue에 0 추가
        else:
            bridge_queue.append(0)

        #

    # truck_weights가 빈 순간, 즉 마지막 팝레프트 된순간 종료되므로, 마지막 애가 지나가는 시간만큼 더해줘야함
    answer = time + bridge_length
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
