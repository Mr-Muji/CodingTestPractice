"""
완주하지 못한 선수
프로그래머스 Lv1
https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
"""


def solution2(participant, completion):
    for runner in participant:
        if runner in completion:
            # participant.remove(runner)
            completion.remove(runner)
        else:
            return runner


def solution3(participant, completion):
    answer = ""

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    answer = participant[-1]

    return answer


def solution4(participant, completion):
    from collections import Counter

    # 참가자와 완주자의 수를 각각 센다.
    count_participant = Counter(participant)
    print(count_participant)
    count_completion = Counter(completion)

    # 완주자 명단을 뺀 차집합에 남은 요소가 완주하지 못한 선수입니다.
    diff = count_participant - count_completion
    return list(diff.keys())[0]


def solution5(participant, completion):

    count = {}
    for runner in participant:
        count[runner] = count.get(runner, 0) + 1

    for c in completion:
        count[c] -= 1

    for name, cnt in count.items():
        if cnt > 0:
            return name


print(solution5(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(
    solution5(
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
    )
)
print(solution5(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
