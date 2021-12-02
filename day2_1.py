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