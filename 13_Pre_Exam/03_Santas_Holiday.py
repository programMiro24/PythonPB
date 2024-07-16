PRICE_FOR_ROOM_FOR_ONE_PERSON_FOR_NIGHT = 18.00
PRICE_FOR_APARTMENT_FOR_NIGHT = 25.00
PRICE_FOR_PRESIDENT_APARTMENT_FOR_NIGHT = 35.00

PERCENT_DISCOUNT_1_10_APARTMENT = 0.30
PERCENT_DISCOUNT_10_15_APARTMENT = 0.35
PERCENT_DISCOUNT_15_APARTMENT = 0.50

PERCENT_DISCOUNT_1_10_PRESIDENT_APARTMENT = 0.10
PERCENT_DISCOUNT_10_15_PRESIDENT_APARTMENT = 0.15
PERCENT_DISCOUNT_15_PRESIDENT_APARTMENT = 0.20

PERCENT_FOR_POSITIVE_GRADE = 0.25
PERCENT_FOR_NEGATIVE_GRADE = 0.10

days_stay = int(input())
nights = days_stay - 1
type_room = input()
grade = input()
price = 0

if type_room == 'room for one person':
    price = nights * PRICE_FOR_ROOM_FOR_ONE_PERSON_FOR_NIGHT
elif type_room == 'apartment':
    price = nights * PRICE_FOR_APARTMENT_FOR_NIGHT
    if days_stay < 10:
        price -= (price * PERCENT_DISCOUNT_1_10_APARTMENT)
    elif days_stay > 15:
        price -= (price * PERCENT_DISCOUNT_15_APARTMENT)
    elif 10 <= days_stay <= 15:
        price -= (price * PERCENT_DISCOUNT_10_15_APARTMENT)
elif type_room == 'president apartment':
    price = nights * PRICE_FOR_PRESIDENT_APARTMENT_FOR_NIGHT
    if days_stay < 10:
        price -= (price * PERCENT_DISCOUNT_1_10_PRESIDENT_APARTMENT)
    elif days_stay > 15:
        price -= (price * PERCENT_DISCOUNT_15_PRESIDENT_APARTMENT)
    elif 10 <= days_stay <= 15:
        price -= (price * PERCENT_DISCOUNT_10_15_PRESIDENT_APARTMENT)

if grade == 'positive':
    price += (price * PERCENT_FOR_POSITIVE_GRADE)
elif grade == 'negative':
    price -= (price * PERCENT_FOR_NEGATIVE_GRADE)

print(f'{price:.2f}')
