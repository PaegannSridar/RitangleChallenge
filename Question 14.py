from word2number import w2n
import inflect

p = inflect.engine()
numbers = []
for i in range(1, 1000):
    numbers.append(p.number_to_words(i))

numbers.sort()
eight = numbers.index('eight')
nine = numbers.index('nine')
print(eight)
print(nine)

total = 0

for i in range(eight+1, nine):
    total = total + w2n.word_to_num(numbers[i])

print(total)