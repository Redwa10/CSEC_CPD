n = int(input())
uniforms = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    home_color = uniforms[i][0]
    for j in range(n):
        if i != j:
            guest_color = uniforms[j][1]
            if home_color == guest_color:
                count += 1

print(count)