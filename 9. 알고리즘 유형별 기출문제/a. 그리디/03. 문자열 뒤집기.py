s = input()

zero_data = 0
one_data = 0

tmp = s[0]
if tmp == '0':
    zero_data += 1
else:
    one_data += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            zero_data += 1
        else:
            one_data += 1

if zero_data == 0 or one_data == 0:
    print(0)
else:
    print(min(zero_data, one_data))