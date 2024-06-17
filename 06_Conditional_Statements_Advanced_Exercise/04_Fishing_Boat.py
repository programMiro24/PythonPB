RENT_SPRING = 3000
RENT_SUMMER_AUTUMN = 4200
RENT_WINTER = 2600

DISCOUNT_6 = 0.10
DISCOUNT_7_11 = 0.15
DISCOUNT_12 = 0.25

ADDICTED_DISCOUNT = 0.05
# If they even

budget = int(input())
season = input()
count_people = int(input())
price = 0

if season == 'Spring':
    price = RENT_SPRING
    if 7 <= count_people <= 11:
        price -= (price * DISCOUNT_7_11)
    elif count_people <= 6:
        price -= (price * DISCOUNT_6)
    else:
        price -= (price * DISCOUNT_12)

elif season == 'Summer' or season == 'Autumn':
    price = RENT_SUMMER_AUTUMN
    if 7 <= count_people <= 11:
        price -= (price * DISCOUNT_7_11)
    elif count_people <= 6:
        price -= (price * DISCOUNT_6)
    else:
        price -= (price * DISCOUNT_12)

elif season == 'Winter':
    price = RENT_WINTER
    if 7 <= count_people <= 11:
        price -= (price * DISCOUNT_7_11)
    elif count_people <= 6:
        price -= (price * DISCOUNT_6)
    else:
        price -= (price * DISCOUNT_12)

if not season == 'Autumn' and count_people % 2 == 0:
    price -= (price * ADDICTED_DISCOUNT)

if budget >= price:
    print(f'Yes! You have {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')
