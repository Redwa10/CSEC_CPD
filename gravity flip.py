n = int(input())
lst1 = []
lst = list(map(int, input().rstrip().split()))
for i in sorted(lst):
    lst1.append(i)
for j in lst1:
    print(j, end=" ")
