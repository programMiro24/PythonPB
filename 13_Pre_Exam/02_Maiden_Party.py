PRICE_FOR_LOVE_MESSAGE = 0.60
PRICE_FOR_WAX_ROSE = 7.20
PRICE_FOR_KEYCHAIN = 3.60
PRICE_FOR_CARTOON = 18.20
PRICE_FOR_LUCKY_SURPRISE = 22
ADDITIONAL_PERCENT = 0.35 # Отстъпка
PERCENT_HOST = 0.10 # Наем

price_for_maiden_party = float(input())
count_love_message = int(input())
count_wax_rose = int(input())
count_keychain = int(input())
count_cartoon = int(input())
count_lucky_surprise = int(input())

result = ''
total_count = count_love_message + count_wax_rose + count_keychain + count_cartoon + count_lucky_surprise

price = (count_love_message * PRICE_FOR_LOVE_MESSAGE
         + count_wax_rose * PRICE_FOR_WAX_ROSE
         + count_keychain * PRICE_FOR_KEYCHAIN
         + count_cartoon * PRICE_FOR_CARTOON
         + count_lucky_surprise * PRICE_FOR_LUCKY_SURPRISE)

if total_count >= 25:
    price -= (price * ADDITIONAL_PERCENT)

price -= (price * PERCENT_HOST)

if price >= price_for_maiden_party:
    diff = price - price_for_maiden_party
    result = f'Yes! {diff:.2f} lv left.'
else:
    diff = price_for_maiden_party - price
    result = f'Not enough money! {diff:.2f} lv needed.'

print(result)
