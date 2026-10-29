import time
import sys
from dictionary import words


def delayPrint(string):
    for char in str(string):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)
        
info = ""
badLetters = ""
goodLetters = ""
wordofDay = "laser"
guessed = [];
won = False
count = 0;

delayPrint("Welcome to Hoover High School's Wordle Wednesday presented by the CS Club!")
print("")
delayPrint("Please guess a 5 letter word (None of our words will repeat letters). You have 6 guesses to guess correctly. If your guess is not 5 characters or it is not a word in our word list, you will be prompted to guess again, but it will not count against your 6 guesses.")
print("")
delayPrint("*letter shows* = Correct, ! = Incorrect Spot, X = Incorrect Input.")
print("")
while count <= 5:
  info = ""
  win = 0
  print("")
  guess = (input("Please type in a guess: ")).lower() 
  while guess in guessed:
      guess = (input("You already guessed that, please type in another guess: ")).lower()
  if len(guess) != 5:
     print("Please try again")
  elif words.count(guess) == 0:
	   print("please try again")
  else:
      for i in range(5):
        if guess[i] == wordofDay[i]:
          info = info + wordofDay[i] + " "
          win += 1
          
          if goodLetters.count(guess[i]) == 0:
              goodLetters = goodLetters + guess[i] + " "
          
        elif wordofDay.count(guess[i]) > 0:
           info = info + "! "
           if goodLetters.count(guess[i]) == 0:
              goodLetters = goodLetters + guess[i] + " "
              
        else:
           info = info + "X "
           if badLetters.count(guess[i]) == 0:
               badLetters = badLetters + guess[i] + " "
           
           
      count += 1
      guessed.append(guess)
      print("")
      delayPrint(info)
      print("")
      if win == 5:
        won = True
        break
      print("")
      delayPrint("Here are the letters not in the word: " + badLetters)
      print("")
      delayPrint("Here are the letters in the word: " + goodLetters)
      print("")
      
      

if won:
  print("")
  print("")
  delayPrint("You won!")
else:
  print("")
  delayPrint("Try again next time!")
  print("")
  delayPrint("The word of the day is " + wordofDay)
  
print("")
delayPrint("Thank you for playing Hoover's Wordle Wednesday. This game is a work in progress, and their... woops... there may be some bugs. If you encountered any problems, we sincerely apologize. We hope to have them resolved soon.")
print("")
delayPrint("Respect")
print("")
delayPrint("Responsibility")
print("")
delayPrint("Integrity")
print("")
delayPrint("Go Bucs!")
