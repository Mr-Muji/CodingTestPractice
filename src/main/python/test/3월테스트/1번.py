"""
입출력 예시

입력
5
watch 2000
scarf 1500
boots 4000
coat 10000
perfume 7000

출력
coat 10000
scarf 1500


"""

import sys
input = sys.stdin.readline

N = int(input().strip())  # 개행 문자 제거

name = []
price = []
for _ in range(N):
    S, P = input().split()
    name.append(S)
    price.append(int(P))

# 가장 비싼 물품 찾기
max_idx = price.index(max(price))
print(name[max_idx], price[max_idx])

# 가장 저렴한 물품 찾기
min_idx = price.index(min(price))
print(name[min_idx], price[min_idx])

"""
내가 푼 풀이는 아래와 같음.


"""
user_input = int(input())
data_dict = {}
num_list = []

for _ in range(user_input):
    name, score = input().strip().split()
    score = int(score)  # 미리 int 변환
    data_dict[score] = name
    num_list.append(score)

if num_list:  # 입력이 0개일 경우 예외 방지
    num_list.sort()
    min_val = num_list[0]
    max_val = num_list[-1]

    print(f"{data_dict[max_val]} {max_val}")
    print(f"{data_dict[min_val]} {min_val}")
