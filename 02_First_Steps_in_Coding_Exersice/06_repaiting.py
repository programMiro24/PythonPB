PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNING = 5.00
PRICE_BAGS = 0.40
ADITTONALLY_PAINT = 0.10
ADITTONALLY_NYLON = 2
WORKER_PRICE_PER_HOUR=0.30

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinning = int(input())
work_hours = int(input())

quantity_nylon += ADITTONALLY_NYLON
quantity_paint += (quantity_paint * ADITTONALLY_PAINT)

total_sum_materials = (quantity_nylon * PRICE_NYLON) \
                       + (quantity_paint * PRICE_PAINT)\
                       + (quantity_thinning * PRICE_THINNING) \
                       + PRICE_BAGS
total_sum_repairs = (total_sum_materials * WORKER_PRICE_PER_HOUR) * work_hours
total_sum = total_sum_repairs + total_sum_materials

print(total_sum)
