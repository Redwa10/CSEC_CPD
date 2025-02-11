lst1 = []
move = 0
for _ in range(5):
    lst = list(map(int, input().rstrip().split()))
    lst1.append(lst)
for i in range(5):
    for j in range(5):
        if lst1[i][j] == 1:
            x, y = i+1, j+1
            break

move = abs(x - 3) + abs(y - 3)
print(move)
