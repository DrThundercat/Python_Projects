import random

#variables
y = 0
tries_message = "you tried %s times"
#get the number
number = int(random.randint(0, 1000))

# screen message 
print("A random number will be generated")
print("Guess the Random number and you win!")

# collect user input
user_value = int(input('enter in a guess: '))

while (user_value != number):
    
    if(user_value > number):
        print('that number is too high')
        y = y + 1
        user_value = int(input('enter in a guess: '))
    elif(user_value < number):
        print('that number is too low')
        y = y + 1
        user_value = int(input('enter in a guess: '))
        
y = y + 1
print("you win!")
print(tries_message % y)
