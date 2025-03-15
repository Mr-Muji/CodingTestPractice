"""
https://kakao-tech-bootcamp.goorm.io/learn/lecture/55237/%ED%8C%90%EA%B5%90-2%EA%B8%B0-%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%85%8C%ED%81%AC-%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B0%95%EC%A2%8C/lesson/2547539/2%EB%B2%88

입출력 예시

입력
4 3 1
2 0 1 5
5
S R R L L
출력
11

입력
4 4 1
4 0 2 3
4
L L L L

출력
12

"""

import sys
import io
# input = sys.stdin.readlines

test_input = """4 3 1
2 0 1 5
5
S R R L L
"""

# StringIO를 활용하여 입력값을 표준 입력처럼 사용
sys.stdin = io.StringIO(test_input)

# map을 사용하여 한번에 int로 저장. 이렇게 하면 int(N) 이렇게 안해줘도 됨.
N, M, X = map(int, input().strip().split())

# N 번 만큼 for문 안돌리고 이렇게 그냥 넣어줘도 된다. 주의할 점은 list로 묶어주어야 한다는 부분임. map 객체는 이터레이터 객체이므로.
tree_list = []
tree_list = list(map(int, input().strip().split()))


print(tree_list)

Q = input().strip()

print(Q)

TOTAL = 0
cnt = 0
for POS in input().strip().split():
    print(POS)
    if tree_list[X - 1] + cnt >= M:   # 현재 위치의 나무 길이가 M 이상이면 자르고 소지 목재량에 추가. 잘랐으므로 나무 높이는 0
        TOTAL += tree_list[X - 1] + cnt
        tree_list[X - 1] = 0
    match POS:  # 이동
        case "L":
            if X == 1:
                X = N
            else:
                X -= 1
        
        case "R":
            if X == N:
                X = 1
            else:
                X += 1

    # 이 부분은 로직상으론 맞으나, 이렇게 하면 시간복잡도가 O(NQ) 가 되어 너무 느려짐. 그래서 cnt 추가해줌
    # for i in range(N):
    #     tree_list[i] += 1
    cnt += 1

print(TOTAL)
