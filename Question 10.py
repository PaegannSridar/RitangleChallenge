import inflect
import re

p = inflect.engine()
sentence_template = "Count carefully and you will see that this sentence contains {word_count} words and between them they contain {vowel_count} vowels."

def calculate_counts(sentence):
    words = re.findall(r'\b\w+\b', sentence) 
    word_count = len(words)
    vowel_count = sum(1 for char in sentence if char.lower() in 'aeiou')
    return word_count, vowel_count

total_sum = 0

for i in range(0, 200):
    for j in range(0, 200):
        sentence = sentence_template.format(word_count=p.number_to_words(i), vowel_count=p.number_to_words(j))
        word_counts, vowels_counts = calculate_counts(sentence)
        if word_counts == i and vowels_counts == j:
            product = i * j
            total_sum += product

print(total_sum)
