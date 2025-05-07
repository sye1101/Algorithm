# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    return answer