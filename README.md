# Number Guessing Game

## Description
This Python script implements a Number Guessing Game where the player selects a range (from a lower bound to an upper bound) and tries to guess a randomly selected number within that range. The game calculates the minimum number of guesses needed based on the range and provides feedback on each guess. The player wins if they guess the number within the allowed attempts; otherwise, they receive a "Better Luck Next Time" message.

## Features
- User-defined range for guessing.
- Automatic calculation of the minimum number of guesses required.
- Feedback on whether the guess was too high or too low.
- Congratulatory message if the user guesses the number correctly within the allowed attempts.
- Encouraging message if the user does not guess the number within the allowed attempts.

## How to Play
1. Input the lower and upper bounds of the guessing range.
2. Try to guess the randomly selected number within the calculated number of attempts.
3. Receive feedback after each guess and see if you guessed the number correctly.
4. The game will end once you either guess the number correctly or run out of attempts.

## Example Gameplay

```plaintext
Enter the lower number : 1
Enter the upper number : 10
You have only 4 chances to guess the correct number.

Enter the guess: 5
You guessed it wrong. The number is greater than 5

Enter the guess: 7
You guessed it wrong. The number is less than 7

Enter the guess: 6
CONGRATULATIONS
YOU ARE A WINNER
You guessed it right in 3 attempts
