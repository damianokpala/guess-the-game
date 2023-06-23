#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

print(logo)
print("Welcome to guess the number game")
level = input("Select difficulty: Hard or Easy: ").lower()

if level == "easy":
  life = 5
  print("You are in an easy level with 5 lifes")
elif level == "hard":
  life = 10
  print("You are in a difficult mode and you have 10 lives ❤️")

rand_num = random.randint(1, 101)

keep_playing = True

while keep_playing:
  user_guess = int(input("Guess a number between 1 and 100: "))

  if user_guess == rand_num:
     print("Hurray 🎉🎉, you won")
     keep_playing == False
  elif user_guess > rand_num:
    print("Too high")
    life = life - 1
    print(f"You have {life} life left")
  elif user_guess < rand_num:
    print("Too low")
    life = life - 1
    print(f"You have {life} life left")
    
  if life == 0:
    print("Sorry, you lose")
    try_again = input("Do you want to continue playing: yes or no").lower()
    if try_again == "no":
       keep_playing = False
    else:
      level = input("Select difficulty: Hard or Easy: ").lower()
      if level == "easy":
        life = 5
        print("You are in an easy level with 5 lifes")
      elif level == "hard":
        life = 10
        print("You are in a difficult mode and you have 10 lives ❤️")
      keep_playing = True

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

