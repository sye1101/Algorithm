"""
K1KA5CB7
"""

"""
AJKDLSI412K4JSJ9D
"""

"""
# 내가 푼 코드
data = input()
sorted_data = ''.join(sorted(data))
value = 0
result = ''

for x in sorted_data:
    if ord(x) < 65:
        value += int(x)
    else:
        result += x

result = result + str(value)

print(result)
"""

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))