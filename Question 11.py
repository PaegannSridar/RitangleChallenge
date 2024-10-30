from datetime import datetime

d = [i for i in range(2,31)]

mm = [i for i in range(1,12)]

yy = [i for i in range(24,99)]

dates = []
for d2 in d:
    for m2 in mm:
        for y2 in yy:
            if m2 > d2 and y2 > m2 and m2 % d2 ==0 and y2 % m2 ==0:
                dates.append([d2,m2,y2])

date_objects = [datetime(2000 + y, m, d) for d, m, y in dates]

date_objects.sort()

max_diff = None
date_pair = None

for i in range(len(date_objects) - 1):
    diff = abs((date_objects[i + 1] - date_objects[i]).days)
    if max_diff is None or diff > max_diff:
        max_diff = diff
        date_pair = (date_objects[i], date_objects[i + 1])

print(f"Largest time difference between adjacent dates: {max_diff} days")
print(f"Dates with the largest difference: {date_pair[0].date()} and {date_pair[1].date()}")