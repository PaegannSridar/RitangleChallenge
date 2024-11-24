import math
from itertools import combinations, permutations


def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False


def is_triangular(num):
    test = 8 * num + 1
    return int(math.sqrt(test)) ** 2 == test


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def are_coprime(*numbers):
    for pair in combinations(numbers, 2):
        if gcd(pair[0], pair[1]) != 1:
            return False
    return True


def find_triplets():
    odd_composites = [n for n in range(11, 100, 2) if is_composite(n)]
    triplets = []

    for triplet in combinations(odd_composites, 3):
        a, b, c = sorted(triplet)
        perimeter = a + b + c

        if a + b > c and is_triangular(perimeter) and are_coprime(a, b, c):
            triplets.append((a, b, c))

    return triplets


results = find_triplets()
for triplet in results:
    print(triplet)
