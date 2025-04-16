def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀의 최대 깊이 초과
recursive_function()