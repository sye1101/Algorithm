# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    answer = []
    length = len(stages)  # 사용자 수

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer