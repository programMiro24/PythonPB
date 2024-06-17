number_1 = int(input())
number_2 = int(input())
operation = input()

text = ''

if operation == '+':

    text = f'{number_1} + {number_2} = {number_1 + number_2}'

    if (number_1 + number_2) % 2 == 0:
        text += ' - even'
    else:
        text += ' - odd'

elif operation == '-':

    text = f'{number_1} - {number_2} = {number_1 - number_2}'

    if (number_1 - number_2) % 2 == 0:
        text += ' - even'
    else:
        text += ' - odd'

elif operation == '*':

    text = f'{number_1} * {number_2} = {number_1 * number_2}'

    if (number_1 * number_2) % 2 == 0:
        text += ' - even'
    else:
        text += ' - odd'

elif number_2 == 0:

    text = f'Cannot divide {number_1} by zero'

elif operation == '/':
    text = f'{number_1} / {number_2} = {(number_1 / number_2):.2f}'

elif operation == '%':

    text = f'{number_1} % {number_2} = {number_1 % number_2}'

print(text)
