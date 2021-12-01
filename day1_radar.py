total = 0 #cumulative term
last = 0 #previous row's value
for row in open('day1_radar.txt'):
    row = int(row.strip()) #convert to int
    if last and row > last: #at least the second data point, and the current value > previous
        total += 1
    last = row

print(total)

