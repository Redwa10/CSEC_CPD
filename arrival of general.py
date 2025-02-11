n = int(input())
lst = list(map(int, input().rstrip().split()))
max_pos = 0
min_pos = 0
for i in range(1, len(lst)+1):
    if lst[i-1] == max(lst):
        max_pos = i
        
    else:
        pass
    if lst[i-1] == min(lst):
        min_pos = i
    else:
       pass
count = (max_pos - 1) + (len(lst) - min_pos - 1)
print(f"{count}")