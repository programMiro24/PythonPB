import math

type_figure = input()

if type_figure == 'square':
    side = float(input())
    area = side * side
elif type_figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif type_figure == 'circle':
    radius = float(input())
    area = math.pi * radius * radius
else:
    side = float(input())
    height = float(input())
    area = (side * height)/2

print(f'{area:.3f}')
