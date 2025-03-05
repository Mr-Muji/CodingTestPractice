"""
동영상 재생기
프로그래머스 Lv1
https://school.programmers.co.kr/learn/courses/30/lessons/340213

enumerate 의 사용

"""


def solution(video_len, pos, op_start, op_end, commands):
    answer = ""
    current_time = get_time(pos)
    if current_time >= get_time(op_start) and current_time <= get_time(op_end):
        current_time = get_time(op_end)

    for i in range(0, len(commands)):
        if commands[i] == "prev":
            current_time -= 10
            if current_time < 0:
                current_time = 0
            if current_time >= get_time(op_start) and current_time <= get_time(op_end):
                current_time = get_time(op_end)
            
        elif commands[i] == "next":
            current_time += 10
            if current_time >= get_time(video_len):
                current_time = get_time(video_len)
            if current_time >= get_time(op_start) and current_time <= get_time(op_end):
                current_time = get_time(op_end)
            

    # print(a, b)

    answer = convert_to_time(current_time)

    return answer


def get_time(str):
    """
    스트링타입 시간을 분으로 바꿔줌.
    """
    a, b = str.split(":")
    full_time = int(a) * 60 + int(b)
    return full_time


def convert_to_time(time):
    a = int(time / 60)
    if a < 10:
        str_a = "0" + str(a)
    else:
        str_a = str(a)

    b = int(time % 60)
    if b < 10:
        str_b = "0" + str(b)
    else:
        str_b = str(b)

    return str_a + ":" + str_b


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
