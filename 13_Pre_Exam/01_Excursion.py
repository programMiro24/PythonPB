PRICE_FOR_NIGHT = 20
PRICE_FOR_TRANSPORT_CARD = 1.60
PRICE_FOR_MUSEUM_TICKET = 6
ADDITIONAL_PROCENT = 0.25

count_people_in_group = int(input())
count_nights = int(input())
count_transport_card = int(input())
count_museum_ticket = int(input())

price_for_one_person = 0
price_for_one_person = (PRICE_FOR_NIGHT * count_nights
         + count_museum_ticket * PRICE_FOR_MUSEUM_TICKET
         + PRICE_FOR_TRANSPORT_CARD * count_transport_card)
price = price_for_one_person * count_people_in_group
price *= 1.25
print(f'{price:.2f}')

