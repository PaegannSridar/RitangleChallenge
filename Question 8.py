import itertools
word = 'RITANGLE'
combinations = list(itertools.permutations(word, 8))
count = 0
for i in combinations:
    vowels = "AEIOU"
    found_adjacent_vowels = False
    for j in range(len(i) - 1):
        if i[j] in vowels and i[j + 1] in vowels:
            found_adjacent_vowels = True
            break
    if found_adjacent_vowels:
        count = count + 1

print(count)