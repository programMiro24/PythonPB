PRICE_NEED_FOR_BG = 100
PRICE_NEED_FOR_BALKANS = 1000
PRICE_NEED_FOR_EUROPE = 1000

PERCENT_BG_SUMMER = 0.30 #CAMP
PERCENT_BG_WINTER = 0.70 #HOTEL
PERCENT_BALKANS_SUMMER = 0.40 #CAMP
PERCENT_BALKANS_WINTER = 0.80 #HOTEL
PERCENT_EUROPE = 0.90 #HOTEL

budget = float(input())
season = input()

price = 0
destination = ''
type_holiday = ''

if season == 'summer':
    if budget <= PRICE_NEED_FOR_BG:
        destination = 'Bulgaria'
        type_holiday = 'Camp'
        price = budget * PERCENT_BG_SUMMER

    elif budget <= PRICE_NEED_FOR_BALKANS:
        destination = 'Balkans'
        type_holiday = 'Camp'
        price = budget * PERCENT_BALKANS_SUMMER

    elif budget > PRICE_NEED_FOR_EUROPE:
        destination = 'Europe'
        type_holiday = 'Hotel'
        price = budget * PERCENT_EUROPE

elif season == 'winter':
    if budget <= PRICE_NEED_FOR_BG:
        destination = 'Bulgaria'
        type_holiday = 'Hotel'
        price = budget * PERCENT_BG_WINTER

    elif budget <= PRICE_NEED_FOR_BALKANS:
        destination = 'Balkans'
        type_holiday = 'Hotel'
        price = budget * PERCENT_BALKANS_WINTER

    elif budget > PRICE_NEED_FOR_EUROPE:
        destination = 'Europe'
        type_holiday = 'Hotel'
        price = budget * PERCENT_EUROPE

print(f'Somewhere in {destination}')
print(f'{type_holiday} - {price:.2f}')
