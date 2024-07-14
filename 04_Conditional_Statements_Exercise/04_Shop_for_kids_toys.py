PRICE_FOR_PUZZLE = 2.60
PRICE_FOR_TALKING_DOLL = 3
PRICE_FOR_TEDDY_BEAR = 4.10
PRICE_FOR_MINION = 8.20
PRICE_FOR_TRUCK = 2

price_for_vacation = float(input())
count_puzzles = int(input())
count_talking_doll = int(input())
count_teddy_bear = int(input())
count_minion = int(input())
count_truck = int(input())
result = ''
discount = 0
budget = count_puzzles * PRICE_FOR_PUZZLE + count_talking_doll * PRICE_FOR_TALKING_DOLL\
    + count_teddy_bear * PRICE_FOR_TEDDY_BEAR + count_minion * PRICE_FOR_MINION \
    + count_truck * PRICE_FOR_TRUCK

total_count = count_puzzles + count_talking_doll + count_teddy_bear + count_minion + count_truck
if total_count >= 50:
   discount = budget * 0.25
budget = budget - discount
budget -= (budget * 0.10)

if budget >= price_for_vacation:
    result = f'Yes! {budget - price_for_vacation:.2f} lv left.'
else:
    result = f'Not enough money! {price_for_vacation - budget:.2f} lv needed.'

print(result)
