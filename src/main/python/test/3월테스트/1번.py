import sys
input = sys.stdin.readline

N = int(input())

name = []
price = []
for _ in range(N):
    S, P = input().split()
    name.append(S)
    price.append(int(P))

# 가장 비싼 물품의 품명과 가격을 구한다.
ans1 = name[0]
ans2 = price[0]
for i in range(1, N):
    if ans2 < price[i]:
        ans1 = name[i]
        ans2 = price[i]
print(ans1, ans2)

# 가장 저렴한 물품의 품명과 가격을 구한다.
ans1 = name[0]
ans2 = price[0]
for i in range(1, N):
    if ans2 > price[i]:
        ans1 = name[i]
        ans2 = price[i]
print(ans1, ans2)