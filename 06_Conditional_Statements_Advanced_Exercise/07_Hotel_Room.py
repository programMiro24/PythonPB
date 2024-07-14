MAY_OCTOBER_STUDIO = 50
MAY_OCTOBER_APARTMENT = 65
JUNE_SEPTEMBER_STUDIO = 75.20
JUNE_SEPTEMBER_APARTMENT = 68.70
JULY_AUGUST_STUDIO = 76
JULY_AUGUST_APARTMENT = 77

DISCOUNT_7_MAY_OCTOBER_STUDIO = 0.05
DISCOUNT_14_MAY_OCTOBER_STUDIO = 0.30
DISCOUNT_14_JUNE_SEPTEMBER_STUDIO = 0.20
DISCOUNT_MORE_14_APARTMENT = 0.10

LIMIT_7 = 7
LIMIT_14 = 14

mount = input()
count_holidays = int(input())
price_studio = 0
price_apartment = 0

if mount == 'May' or mount == 'October':
    price_studio = count_holidays * MAY_OCTOBER_STUDIO
    price_apartment = count_holidays * MAY_OCTOBER_APARTMENT
    if count_holidays > LIMIT_14:
        price_studio -= (price_studio * DISCOUNT_14_MAY_OCTOBER_STUDIO)
    elif count_holidays > LIMIT_7:
        price_studio -= (price_studio * DISCOUNT_7_MAY_OCTOBER_STUDIO)

elif mount == 'September' or mount == 'June':
    price_studio = count_holidays * JUNE_SEPTEMBER_STUDIO
    price_apartment = count_holidays * JUNE_SEPTEMBER_APARTMENT
    if count_holidays > LIMIT_14:
        price_studio -= (price_studio * DISCOUNT_14_JUNE_SEPTEMBER_STUDIO)
else:
    price_studio = count_holidays * JULY_AUGUST_STUDIO
    price_apartment = count_holidays * JULY_AUGUST_APARTMENT

if count_holidays > 14:
    price_apartment -= (price_apartment * DISCOUNT_MORE_14_APARTMENT)

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')

