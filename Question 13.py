import itertools

lst = []
for i in range(5):
    for j in range(6):
        lst.append(j + 1)

rolls = list(set(itertools.combinations(lst, 5)))

count = 0
count3 = 0

for i in rolls:
    count2 = 0
    count += 1
    for j in itertools.combinations(i, 3):
        if (j[0] + j[1] > j[2]) and (j[0] + j[2] > j[1]) and (j[1] + j[2] > j[0]):
            count2 += 1

    if count2 == 0:
        count3 += 1

print(count3 / count)