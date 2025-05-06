# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = len(s)

    # 완전 탐색 진행
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        # 남은 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(len(compressed), answer)
    return answer