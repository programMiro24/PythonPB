import math
up_limit_first_number = int(input())
up_limit_second_number = int(input())
up_limit_third_number = int(input())

for f in range(1, up_limit_first_number + 1):
    if f % 2 == 1:
        continue
    for s in range(1, up_limit_second_number + 1):
        is_prime = True
        for d in range(2, int(math.sqrt(s)) + 1):
            if s % d == 0:
                is_prime = False
                continue
        if not is_prime:
            continue
        if s == 1 or s > 7:
            continue
        for t in range(1, up_limit_third_number + 1):
            if t % 2 == 1:
                continue
            print(f'{f} {s} {t}')
