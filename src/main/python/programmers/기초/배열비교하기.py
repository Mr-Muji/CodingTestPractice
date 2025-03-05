"""
배열 비교하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181856

배열 길이 측정은 len(arr) 이다.
arr.length() 가 아니다..

"""


def solution(arr1, arr2):
    answer = 0
    a = len(arr1)
    b = len(arr2)
    if a < b:
        answer = -1
    elif a == b:
        if sum(arr1) < sum(arr2):
            answer = -1
        elif sum(arr1) == sum(arr2):
            answer = 0
        else:
            answer = 1
    else:
        answer = 1

    return answer


print(solution([49, 13], [70, 11, 2]))
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))
