#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1] - prices[0]
  current_min = prices[0]
  #1 is the start
  for price in prices[1:]:
    if price < current_min:
      current_min = price
    elif price - current_min > max_profit:
      max_profit = price - current_min
  return max_profit

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))