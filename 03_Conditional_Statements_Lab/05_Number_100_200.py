number = int(input())
result = ''
if number < 100:
    result = 'Less than 100'
if 100 <= number <= 200:
    result = 'Between 100 and 200'
if number > 200:
    result = 'Greater than 200'
print(result)
