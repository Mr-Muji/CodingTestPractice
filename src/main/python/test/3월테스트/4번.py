"""

https://kakao-tech-bootcamp.goorm.io/learn/lecture/55237/%ED%8C%90%EA%B5%90-2%EA%B8%B0-%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%85%8C%ED%81%AC-%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B0%95%EC%A2%8C/lesson/2547545/4%EB%B2%88-%ED%95%B4%EC%84%A4
"""

n, k = input().strip().split(" ")
n = int(n)
k = int(k)

nemo = dict()

for i in range(n):
    user_input = input().strip().split(" ")
    for j, value in enumerate(user_input):
        input_str = str(i) + "," + str(j)
        nemo[input_str] = int(value)

# print("nemo = ")
# print(nemo)
# print(nemo.get("3,2", 0))

answer = 0
all_flags = 0

for i in range(n):
    for j in range(n):
        i_0 = str(i) + "," + str(j)
        # print("i  = " + i_0)
        if nemo.get(i_0, 0) == 1:
            continue
        i_1 = str(i - 1) + "," + str(j - 1)
        i_2 = str(i - 1) + "," + str(j)
        i_3 = str(i - 1) + "," + str(j + 1)
        i_4 = str(i) + "," + str(j - 1)
        i_5 = str(i) + "," + str(j + 1)
        i_6 = str(i + 1) + "," + str(j - 1)
        i_7 = str(i + 1) + "," + str(j)
        i_8 = str(i + 1) + "," + str(j + 1)
        all_flags = (
            nemo.get(i_1, 0)
            + nemo.get(i_2, 0)
            + nemo.get(i_3, 0)
            + nemo.get(i_4, 0)
            + nemo.get(i_5, 0)
            + nemo.get(i_6, 0)
            + nemo.get(i_7, 0)
            + nemo.get(i_8, 0)
        )

        # print(all_flags)

        if all_flags == k:
            answer += 1
        all_flags = 0

print(answer)
