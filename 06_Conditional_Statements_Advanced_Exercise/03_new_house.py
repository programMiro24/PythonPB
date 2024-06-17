PRICE_ROSES = 5
PRICE_DAHLIAS = 3.8
PRICE_TULIPS = 2.8
PRICE_NARCISSUS = 3
PRICE_GLADIOLUS = 2.50

PERCENT_FOR_80_ROSES_DISC = 0.10
PERCENT_FOR_90_DAHLIAS_DISC = 0.15
PERCENT_FOR_80_TULIPS_DISC = 0.15
PERCENT_FOR_120_NARCISSUS_IN = 0.15
PERCENT_FOR_80_GLADIOULUS_IN = 0.20

type_flower = input()
count_flowers = int(input())
budget = int(input())
price = 0

if type_flower == 'Roses':
    price = count_flowers * PRICE_ROSES
    if count_flowers > 80:
        price -= (price * PERCENT_FOR_80_ROSES_DISC)

elif type_flower == 'Dahlias':
    price = count_flowers * PRICE_DAHLIAS
    if count_flowers > 90:
        price -= (price * PERCENT_FOR_90_DAHLIAS_DISC)

elif type_flower == 'Tulips':
    price = count_flowers * PRICE_TULIPS
    if count_flowers > 80:
        price -= (price * PERCENT_FOR_80_TULIPS_DISC)

elif type_flower == 'Narcissus':
    price = count_flowers * PRICE_NARCISSUS
    if count_flowers < 120:
        price += (price * PERCENT_FOR_120_NARCISSUS_IN)

else:
    price = count_flowers * PRICE_GLADIOLUS
    if count_flowers < 80:
        price += (price * PERCENT_FOR_80_GLADIOULUS_IN)

if budget >= price:
    print(f'Hey, you have a great garden with {count_flowers} {type_flower} and {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(price - budget):.2f} leva more.')
