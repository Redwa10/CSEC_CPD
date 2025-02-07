n = int(input())
lst = []
count = 0
for _ in range(n):
    char = input()
    lst.append(char)
for j in range(len(lst) - 1):
    if lst[j] != lst[j+1]:
        count += 1
print(count + 1)