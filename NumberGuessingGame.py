#Game: Number Guessing Game

import random  
import math

lower  = int(input("Enter the lower number : "))
upper  = int(input("Enter the upper number : "))

x = random.randint(lower, upper)

total_chances = math.ceil(math.log(upper-lower + 1,2))
print(total_chances)
print("You have only",total_chances,"chances to guess the correct number.")

count = 0
flag = False

while count < total_chances:
    count += 1
    guess = int(input("Enter the guess: "))
    if x == guess:
        print("CONGRATULATIONS")
        print("YOU ARE A WINNER")
        print("You guessed it right in ", count, "attempt")
        flag = True
        break
    elif x > guess:
        print("You guessed it wrong. The number is greater than", guess)
    elif x < guess:
        print("You guessed it wrong. The number is less than", guess)

if not flag:
     print("You didn't guess the number. The number is ", x)
     print("Better Luck Next Time!!!!!!!!!")

# OVER AND END
