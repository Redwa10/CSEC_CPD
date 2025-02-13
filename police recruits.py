n = int(input())
lst = list(map(int, input().rstrip().split()))
available_officers = 0
untreated_crimes = 0
for i in lst:
    if i  > 0:
        available_officers += i
    elif i == -1:
        if available_officers == 0:
            untreated_crimes += 1
        else:
            available_officers -= 1
print(untreated_crimes)