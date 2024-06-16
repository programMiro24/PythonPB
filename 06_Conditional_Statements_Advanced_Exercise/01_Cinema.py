PRICE_PREMIERE = 12
PRICE_NORMAL = 7.5
PRICE_DISCOUNT = 5

type_cinema = input()
rows = int(input())
columns = int(input())

cinema_seats = rows * columns
price = 0

if type_cinema == 'Premiere':
    price = cinema_seats * PRICE_PREMIERE
elif type_cinema == 'Normal':
    price = cinema_seats * PRICE_NORMAL
else:
    price = cinema_seats * PRICE_DISCOUNT

print(f'{price:.2f} leva.')
