a1, a2, a3, a4 =  map(int, input().rstrip().split())
cal =[a1, a2, a3, a4]
str1 = input()
counter = 0
for i in str1:
    counter += cal[int(i)-1]
print(counter)