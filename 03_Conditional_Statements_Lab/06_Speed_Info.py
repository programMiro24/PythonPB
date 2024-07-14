speed = float(input())

result = ''

if speed <= 10:
    result = 'slow'
elif 10 < speed <= 50:
    result = 'average'
elif 50 < speed <= 150:
    result = 'fast'
elif 150 < speed <= 1000:
    result = 'ultra fast'
else:
    result = 'extremely fast'

print(result)
