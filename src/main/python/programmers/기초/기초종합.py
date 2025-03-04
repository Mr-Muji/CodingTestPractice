"""
기초 여러개 합친거
"""


def solution1(input):
    str, n = input.strip().split(" ")
    n = int(n)
    print(str * n)


# solution1("string 5")
"""문자열 곱하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181940
"""


def solution2(my_string, k):
    answer = ""
    answer = my_string * k
    return answer


# print(solution2("string", 3))
# print(solution2("love", 10))

"""공배수
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181939
"""
def solution3(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0

    return answer


print(solution3(60, 2, 3))
print(solution3(55, 10, 5))
