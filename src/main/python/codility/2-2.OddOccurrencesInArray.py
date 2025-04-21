"""
XOR, Counter 써서 풀어보기
"""

def solution(A):
    """
    시간복잡도 고려 안함O(n**2)임.
    """
    answer = 0
    list = []
    for a in A:
        if a in list:
            list.remove(a)
        else:
            list.append(a)

    answer = list[0]

    return answer


def solution2(A):
    answer = 0
    list = []
    hashmap = dict()

    for a in A:
        hashmap.get(a, 0)


print(solution2([9, 3, 9, 3, 9, 7, 9]))