PRICE_FOR_SEA = 680
PRICE_FOR_MOUNTAIN = 499

count_sea_excursions = int(input())
count_mountain_excursions = int(input())

price = 0
result = ''

while True:
    type_packet = input()
    if type_packet == 'Stop':
        result = f'Profit: {price} leva.'
        break

    if type_packet == 'sea':
        if count_sea_excursions > 0:
            price += PRICE_FOR_SEA
            count_sea_excursions -= 1
    elif type_packet == 'mountain':
        if count_mountain_excursions > 0:
            price += PRICE_FOR_MOUNTAIN
            count_mountain_excursions -= 1
    if count_sea_excursions == 0 and count_mountain_excursions == 0:
        result = f'Good job! Everything is sold.\nProfit: {price} leva.'
        break

print(result)
