n= input()
l = 0
u = 0
for i in range(len(n)):
    if n[i].islower():
        l = l + 1
    elif n[i].isupper():
        u = u + 1
if l > u:
    print(n.lower())
elif u > l:
    print(n.upper())
else:
    print(n.lower())