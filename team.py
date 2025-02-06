n = int(input())
counter = 0
for i in range(n):
    lst = list(map(int, input().rstrip().split()))
    if sum(lst) >= 2:
        counter = counter + 1
    else:
        pass
print(counter)