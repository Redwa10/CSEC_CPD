n = int(input())
lst = list(input())
count = 0
left = 0
while left < n - 1:
    right = left + 1
    if lst[left] == lst[right]:
        count += 1
    else:
        pass
    left += 1
print(count)
