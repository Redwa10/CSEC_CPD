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

max_pos = max_pos - 1
min_pos = len(lst) - min_pos - 1
count = max_pos + min_pos
print(f"{count}")