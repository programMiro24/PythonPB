PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEGETARIAN_MENU = 8.15
DELIVERY_PRICE= 2.50
DESERT_PERCENT = 0.20

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegetarian_menus = int(input())

total_sum_menus = (count_chicken_menus * PRICE_CHICKEN_MENU) \
                  + (count_fish_menus * PRICE_FISH_MENU) \
                  +(count_vegetarian_menus * PRICE_VEGETARIAN_MENU)

total_sum = total_sum_menus + (total_sum_menus * DESERT_PERCENT) + DELIVERY_PRICE

print(total_sum)