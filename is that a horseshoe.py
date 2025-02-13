s1, s2, s3, s4 = map(int, input().split())
unique_colors = len(set([s1, s2, s3, s4]))
needed_horseshoes = 4 - unique_colors
print(needed_horseshoes)