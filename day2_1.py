horz = 0 #horizontal position
depth = 0 #depth position
for line in open('day2_input.txt'):
    action , value = line.split() # split the line into the action and the value
    value = int(value) #convert to int
    if action == 'forward':
        horz += value
    if action == 'down':
        depth += value
    if action == 'up':
        depth -= value

print(horz*depth)

#second question

horz = 0 #horizontal position
depth = 0 #depth position
aim = 0 #aim
for line in open('day2_input.txt'):
    action , value = line.split() # split the line into the action and the value
    value = int(value) #convert to int
    if action == 'forward':
        horz += value
        depth += aim*value
    if action == 'down':
        aim += value
    if action == 'up':
        aim -= value

print(horz*depth)