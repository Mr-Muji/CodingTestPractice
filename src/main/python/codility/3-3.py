def solution(A):
    L = len(A)
    S1 = 0
    S2 = 0
    total = sum(A)
    result = float("inf")

    for i in range(1, L):
        S1 = S1 + A[i - 1]
        S2 = total - S1
        if result > abs(S1 - S2):
            result = abs(S1 - S2)

    return result


print(solution([3, 1, 2, 4, 3]))
