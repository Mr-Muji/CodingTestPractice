"""
괄호의 값

난이도: 실버 1

https://www.acmicpc.net/problem/2504

isinstance(top, int) -> top가 인트인지 판단
type(top) == int
"""
import sys
input = sys.stdin.readline

def solution(s):
    if not s:
        return 0
    stack = []

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if temp == 0 else 2 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0
        elif ch == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if temp == 0 else 3 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    result = 0
    for item in stack:
        if isinstance(item, int):
            result += item
        else:
            return 0
    
    return result


s = input().strip()
print(solution(s))