"""
의상
프로그래머스 Lv2  - 해시
https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""


def solution(clothes):
    answer = 0
    dict = {}

    for cloth, a in clothes:
        dict[a] = dict.get(a, 0) + 1

    # print(dict)

    answer = 1
    for v in dict.values():
        answer *= v + 1

    return answer - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)
print(
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
)
