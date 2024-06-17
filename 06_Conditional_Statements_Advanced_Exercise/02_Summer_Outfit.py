LIMIT_DEGREES_10 = 10
LIMIT_DEGREES_18 = 18
LIMIT_DEGREES_24 = 24
LIMIT_DEGREES_25 = 25

degrees = int(input())
time_of_day = input()

outfit = ' '
shoes = ' '

if time_of_day == 'Morning':

    if LIMIT_DEGREES_10 <= degrees <= LIMIT_DEGREES_18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'

    elif LIMIT_DEGREES_18 < degrees <= LIMIT_DEGREES_24:
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif degrees >= LIMIT_DEGREES_25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time_of_day == 'Afternoon':

    if LIMIT_DEGREES_10 <= degrees <= LIMIT_DEGREES_18:
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif LIMIT_DEGREES_18 < degrees <= LIMIT_DEGREES_24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

    elif degrees >= LIMIT_DEGREES_25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

else:

    if LIMIT_DEGREES_10 <= degrees <= LIMIT_DEGREES_18:
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif LIMIT_DEGREES_18 < degrees <= LIMIT_DEGREES_24:
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif degrees >= LIMIT_DEGREES_25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
