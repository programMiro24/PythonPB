budget = float(input())
count_actor = int(input())
price_for_one_actor = float(input())

result = ''

price_costumes = price_for_one_actor * count_actor
price_decor = 0.10 * budget
if count_actor > 150:
    price_costumes -= (price_costumes * 0.10)
total_price = price_decor + price_costumes
if total_price > budget:
    result = f'Not enough money!\nWingard needs {total_price - budget:.2f} leva more.'
else:
    result = f'Action!\nWingard starts filming with {budget - total_price:.2f} leva left.'
print(result)
