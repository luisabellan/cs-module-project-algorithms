#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here

  target = amount
  coins = denominations
  ways = [1]+[0]*target
  for coin in coins:
      for i in range(coin,target+1):
          ways[i]+=ways[i-coin]
  ways = ways[target] 
  #print(ways)
  return ways


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")