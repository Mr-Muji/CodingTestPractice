def solution(A):
    """
    내가 푼 방식.
    """
    L = len(A)
    seen = []

    for i in range(L + 1):
        seen.append(0)

    for num in A:
        seen[num - 1] = 1

    for i, num in enumerate(seen):
        if num == 0:
            return i + 1
def solution(A):
    """
    내꺼 훨씬 간결하게. -1 +1 안해줘도되서 훨씬 직관적
    
    """
    N = len(A)
    seen = [False] * (N + 2)  # 인덱스 1~N+1까지 사용

    for a in A:
        seen[a] = True

    for i in range(1, N + 2):
        if not seen[i]:
            return i
def solution0(A):
    """
    내가 푼 방식 좀 더 간단하게. seen 배열 정의할 때 쉽게. * 해서 한번에 초기화
    """
    N = len(A)
    seen = [False] * (N + 1)

    for num in A:
        seen[num - 1] = True

    for i in range(N + 1):
        if not seen[i]:
            return i + 1
        

def solution2(A):
    """
    등차수열의 합을 이용한 풀이
    """
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum


def solution3(A):
    """
    XOR 연산을 이용한 풀이
    """
    N = len(A)
    result = 0

    for i in range(1, N + 2):
        result ^= i

    for num in A:
        result ^= num

    return result

