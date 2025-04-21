"""
FrogRiverOne

"""

def solution(X, A):
    
    SUM = X*(X+1)/2
    s = set()
    trigger = False
    current_sum = 0

    for i, a in enumerate(A):
        if a == X:
            trigger = True
        if a <= X and a not in s:
            s.add(a)
            current_sum += a
        if trigger == True and current_sum == SUM:
            return i

    return -1


def solution(X, A):
    covered = set()
    for time, position in enumerate(A):
        if 1 <= position <= X:
            covered.add(position)
            if len(covered) == X:
                return time
    return -1