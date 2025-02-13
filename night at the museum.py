str1 = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = 0
c_letter = 'a'
for i in str1:
    c_pos = alphabet.index(c_letter)
    t_pos = alphabet.index(i)
    c_moves = (t_pos - c_pos)%26
    cc_moves = (c_pos - t_pos)%26
    counter += min(c_moves, cc_moves)
    c_letter = i
print(counter)
