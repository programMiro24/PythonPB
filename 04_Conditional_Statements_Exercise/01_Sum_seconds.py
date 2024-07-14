import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

result = ''

sum_seconds = time_third + time_first + time_second
minute = int(abs(sum_seconds / 60))
seconds = math.floor(sum_seconds % 60)

if seconds < 10:
    result = f'{minute}:0{seconds}'
else:
    result = f'{minute}:{seconds}'

print(result)
