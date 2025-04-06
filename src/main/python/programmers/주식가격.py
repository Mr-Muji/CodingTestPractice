"""
주식가격
프로그래머스 Lv2
스택/큐, DP로도 가능
https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""

# 문제 이해 확실히하게 ( 완전히 잘못 이해하고 있었음)
# 해시 쓰는 법 다시
# 큐 쓰는 법 다시
# enumerate ( inumerate 아님!)
# 이중ㅇ배열 선언 주의 -> 이중배열도 a[[]] 가 아니고 그냥 a[] 임!


def solution(prices):
    prices_len = len(prices)
    answer = [0] * prices_len

    stack = []

    for i, price in enumerate(prices):

        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        i = stack.pop()
        answer[i] = prices_len - i - 1

    return answer


print(solution([1, 2, 3, 2, 3]))
