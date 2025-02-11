n= int(input())
s = 0
d = 0
left = 0
right = n - 1
turn = 0
lst = list(map(int, input().rstrip().split()))

while left <= right:
    if lst[left] > lst[right]:
        count = lst[left]
        left += 1
    else:
        count = lst[right]
        right -= 1
    if turn == 0:
        s += count
    else:
        d += count
    turn = 1 - turn

print(f"{s} {d}")