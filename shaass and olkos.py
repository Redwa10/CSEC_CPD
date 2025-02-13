n = int(input())
birds = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    left_birds = y
    right_birds = birds[x] - y - 1
    
    if x > 0:
        birds[x - 1] += left_birds
    if x < n - 1:
        birds[x + 1] += right_birds
    
    birds[x] = 0

for count in birds:
    print(count)