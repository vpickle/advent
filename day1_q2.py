row = [int(row.strip()) for row in open('day1_radar.txt')] #convert to int
total = 0
for index in range(0,len(row) -3):
        if row[index] + row[index +1] + row[index +2] < row[index+1] + row[index +2] + row[index +3]:
            total +=1
print(total)