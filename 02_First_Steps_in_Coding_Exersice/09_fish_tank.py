CM_TO_LITER = 1000

legth = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume_fish_tank = legth * width * height
volume_litres = volume_fish_tank / LITER_TO_ML
needed_litres = volume_litres * (1 - percent)

print(needed_litres)

