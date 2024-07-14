started_points = int(input())
bonus_points = 0
if started_points < 100:
    bonus_points = 5
elif started_points > 1000:
    bonus_points = started_points * 0.10
elif started_points > 100:
    bonus_points = started_points * 0.20

if started_points % 2 == 0:
    bonus_points += 1
elif started_points % 10 == 5:
    bonus_points += 2

final_points = started_points + bonus_points
result = f'{bonus_points}\n{final_points}'
print(result)