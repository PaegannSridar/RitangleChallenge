import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_primitive_triplets(limit):
    triplets = []
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                if a > b:
                    a, b = b, a
                if c < limit:
                    triplets.append((a, b, c))
    return triplets

"""For all two digit numbers"""
"""limit = 1000
triplets = generate_primitive_triplets(limit)
for triplet in triplets:
    count = 0
    for number in triplet:
        if len(str(number)) == 2:
            count += 1
    if count == 3:
        print(triplet)"""


limit = 1000
triplets = generate_primitive_triplets(limit)
for triplet in triplets:
    count1 = 0
    count2 = 0
    for number in triplet:
        if len(str(number)) == 2:
            count1 += 1
        if len(str(number)) == 3:
            count2 += 1
    if count1 == 1 and count2 == 2:
        print(triplet)
