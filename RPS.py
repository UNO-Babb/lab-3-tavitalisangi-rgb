#RPS.py
#Name: TavitaAfata
#Date: 14 Sep 2025
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y": 
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
    player1 = input("Select Rock, Paper, Scissors (R,P,S): ")
    print("Player chose:", player1)
    options = ["R", "P", "S"]
    computer = random.choice(options)
    print("Computer chose:", computer)

    if player1 == "R" and computer == "R":
      print("Tie")
      ties = ties +1
    if player1 == "R" and computer == "P":
      print("LOSER!")
      losses = losses +1
    if player1 == "R" and computer == "S":
      print("Win")
      wins = wins +1
    if player1 == "P" and computer == "P":
      print("Tie")
      ties = ties +1
    if player1 == "P" and computer == "S":
      print("LOSER!")
      losses = losses +1
    if player1 == "P" and computer == "R":
      print("Win")
      wins = wins +1
    if player1 == "S" and computer == "S":
      print("Tie")
      ties = ties +1
    if player1 == "S" and computer == "R":
      print("LOSER!")
      losses = losses +1
    if player1 == "S" and computer == "P":
      print("Win")
      wins = wins +1
  
    playAgain = input("Play again? (Y/N); ")


  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
