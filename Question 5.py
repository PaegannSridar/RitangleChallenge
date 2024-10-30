import itertools

factors = [1, 3, 5, 9, 15, 25, 27, 45, 75, 81, 135, 225, 405, 675, 2025]

solutions = []

for f1, f2, f3 in itertools.combinations_with_replacement(factors, 3):
    if f1 * f2 * f3 == 2025:
        a = f1 - 1
        B = f2 - 1
        c = f3 - 1
        solutions.append((a, B, c))

for solution in solutions:
    print(f"Solution: a = {solution[0]}, B = {solution[1]}, c = {solution[2]}")
