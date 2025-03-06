"""
동영상 재생기
프로그래머스 Lv1
https://school.programmers.co.kr/learn/courses/30/lessons/340213

enumerate 의 사용
// 연산
iterable 객체의 for문 사용법

"""


def solution(video_len, pos, op_start, op_end, commands):

    video_len = to_second(video_len)
    pos = to_second(pos)
    op_start = to_second(op_start)
    op_end = to_second(op_end)

    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end

        if command == "prev":
            pos = max(0, pos - 10)
        elif command == "next":
            pos = min(video_len, pos + 10)

    if op_start <= pos <= op_end:
        pos = op_end

    return to_time_str(pos)


def to_second(time_str):
    """
    str 형식의 시간을 받아서 초 단위로 변환해주는 함수
    """
    mm, ss = map(int, time_str.split(":"))
    return mm * 60 + ss


def to_time_str(seconds):
    """
    초 단위의 시간을 받아서, "xx:xx" 형태의 str로 바꿔서 변환
    """
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02}:{ss:02}"


"""
입출력 예
video_len	pos	op_start	op_end	commands	result
"34:33"	"13:00"	"00:55"	"02:55"	["next", "prev"]	"13:00"
"10:55"	"00:05"	"00:15"	"06:55"	["prev", "next", "next"]	"06:55"
"07:22"	"04:05"	"00:15"	"04:07"	["next"]	"04:17"
"""


print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))
