n= int(input())
str1 = input()
counter = 0
for i in range(1, n):
    if str1[i] == str1[i-1]:
        counter = counter + 1
    else:
        pass
print(counter)