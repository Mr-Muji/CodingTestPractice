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


# print(solution3(60, 2, 3))
# print(solution3(55, 10, 5))

"""
뒤에서 5등까지
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181853
"""


def solution4(num_list):
    num_list.sort()
    answer = num_list[0:5]
    return answer


# print(solution4([12, 4, 15, 46, 38, 1, 14]))

"""홀짝에 따라 다른 값 반환하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181935
"""


def solution5(n):
    answer = 0
    if n % 2 == 1:
        list = [i * 2 - 1 for i in range(1, n // 2 + 2)]
    else:
        list = [(i * 2) ** 2 for i in range(1, n // 2 + 1)]
    # print(list)
    # for i in list:
    #     answer += i
    answer = sum(list)

    # list(map(lambda x: x * 2, list = [i for i in range(:n/2+1)]))
    # if(n%2 == 1):

    return answer


# print(solution5(10))

"""대소문자 바꿔서 출력하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181949
"""


def solution6(my_string):
    str = my_string.swapcase()
    return str


# print(solution6("aBcDeFg"))

"""
특수문자 출력하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181948
"""


def solution7():
    print("!@#$%^&*(\\'\"<>?:;")


# solution7()

"""
덧셈식 출력하기
프로그래머스 기초
https://school.programmers.co.kr/learn/courses/30/lessons/181947
"""


def solution8(a, b):
    print(f"{a} + {b} = {a + b}")


# solution8(4, 5)


def solution9(str):
    str1, str2 = str.strip().split(" ")
    print(str1 + str2)


# solution9("apple pen")


def solution10(str):
    for i in str:
        print(i)


# solution10("abcde")


def solution11(n):
    if n % 2 == 0:
        print(str(n) + " is even")
    else:
        print(str(n) + " is odd")


# solution11(100)


