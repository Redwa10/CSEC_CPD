from math import gcd

Y, W = map(int, input().split())
max_roll = max(Y, W)
winning_rolls = 7 - max_roll
numerator = winning_rolls
denominator = 6

if numerator == 0:
    print("0/1")
elif numerator == 6:
    print("1/1")
else:
    common_divisor = gcd(numerator, denominator)
    print(f"{numerator // common_divisor}/{denominator // common_divisor}")