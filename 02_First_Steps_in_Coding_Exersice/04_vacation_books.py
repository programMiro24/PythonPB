pages_book = int(input())
pages_per_hour=int(input())
count_days_for_read = int(input())

total_time = pages_book // pages_per_hour
needed_time = total_time // count_days_for_read

print(needed_time)