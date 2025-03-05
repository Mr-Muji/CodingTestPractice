"""
삼총사
프로그래머스 Lv1
https://school.programmers.co.kr/learn/courses/30/lessons/131705

파이썬도 number[i] 같은 사용이 가능하다.
combinations 쓰는 법(임포트, 시간복잡도)
투포인터(처음에 sort 해주는 이유, 시간복잡도가 낮은 이유)

"""

from itertools import combinations


def solution(number):
    answer = 0
    length = len(number)

    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer


def solution2(number):
    """
    콤비네이션을 이용한 풀이. 
    from itertools import combinations  추가해줘야 함. 코드 젤 위에 임포트해줘도 되고,
    def 안에다가 임포트해줘도 됨.
    그런데 결국 시간복잡도는 위의 3중 for문과 같은 O(n^3)이다.
    """
    count = 0
    for trio in combinations(number, 3):
        if sum(trio) == 0:
            count += 1
    return count


def solution3(number):
    number.sort()  # 정렬 (O(n log n))
    n = len(number)
    count = 0

    for i in range(n - 2):  # 첫 번째 숫자 고정 (O(n))
        left, right = i + 1, n - 1  # 두 번째, 세 번째 숫자의 위치
        while left < right:  # 투 포인터 탐색 (O(n))
            total = number[i] + number[left] + number[right]
            if total == 0:
                count += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return count  # 최종 삼총사 개수 반환


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))
