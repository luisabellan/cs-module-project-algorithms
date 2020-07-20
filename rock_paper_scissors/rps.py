#!/usr/bin/python

import sys
from random import randint

def rock_paper_scissors(n):

  #create a list of play options

  n = ["rock", "paper", "scissors"]

  #assign a random play to the computer
  computer = n[randint(0,2)]

  #set player to False
  player = False

  while player == False:

  #set player to True
      player = input("rock, paper, scissors? (Press q to quit):" )

      if player == "q":
          return "Bye"
      elif player == computer:
          print("Tie!")
      elif player == "rock":
          if computer == "paper":
              print("You lose!", computer, "covers", player)
          else:
              print("You win!", player, "smashes", computer)
      elif player == "paper":
          if computer == "scissors":
              print("You lose!", computer, "cut", player)
          else:
              print("You win!", player, "covers", computer)
      elif player == "scissors":
          if computer == "rock":
              print("You lose...", computer, "smashes", player)
          else:
              print("You win!", player, "cut", computer)
      
      else:
          print("That's not a valid play. Check your spelling!")
      #player was set to True, but we want it to be False so the loop continues
      player = False
      computer = n[randint(0,2)]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')