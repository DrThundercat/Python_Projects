import random

print ("Good Luck!!")

numb_rolls = input('how many rolls: ')
if not numb_rolls:
    numb_rolls = 20

max_range = input('how many sides: ')
if not max_range:
    max_range = 6

y = 0
#while (y < int(numb_rolls)):
for x in range(0,int(numb_rolls)):
    print(random.randint(1,int(max_range)))
    #y = y +1

print ("enjoy!")
