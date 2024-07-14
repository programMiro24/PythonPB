import math

MINUTE_AFTER = 15
started_hour = int(input())
started_minute = int(input())

result = ''

minute = started_hour * 60 + started_minute
minute += MINUTE_AFTER
hour = abs(minute // 60)
minute = math.floor(minute % 60)

if hour == 24:
    hour = 0

if minute < 10:
    result = f'{hour}:0{minute}'
else:
    result = f'{hour}:{minute}'

print(result)
