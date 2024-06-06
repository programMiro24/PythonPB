deposit_amount = float(input())
deposit_term = int(input())
annual_percent = float(input())/100

total_amount = deposit_amount + deposit_term * ((deposit_amount * annual_percent) / 12)

print(total_amount)