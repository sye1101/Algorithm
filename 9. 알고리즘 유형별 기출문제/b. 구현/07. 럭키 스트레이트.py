# N: 현재 캐릭터의 점수
n = input()
mid = len(n) // 2

left_sum = 0 # 왼쪽 합
right_sum = 0 # 오른쪽 합

for i in range(len(n)):
    if i < mid:
        left_sum += int(n[i])
    else:
        right_sum += int(n[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')