  #!/usr/bin/python

import sys
import itertools

#
#list of 
rock = ["rock"]
paper = ["paper"]
scissors = ["scissors"]
rps = [rock,paper,scissors]
available_options = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
  if n==0:
    return [[]]
  if n==1:
    return rps
  return rps_helper(n,rock)+rps_helper(n,paper)+rps_helper(n,scissors)

def rps_helper(n,list):
  if n ==1:
    return list
  if n ==2:
    rock_list=list.copy()
    paper_list=list.copy()
    scissor_list=list.copy()
    rock_list.extend(rock)
    paper_list.extend(paper)
    scissor_list.extend(scissors)
    n-=1
    return [rps_helper(n,rock_list), rps_helper(n,paper_list), rps_helper(n,scissor_list)]
  else:
    rock_list=list.copy()
    paper_list=list.copy()
    scissor_list=list.copy()
    rock_list.extend(rock)
    paper_list.extend(paper)
    scissor_list.extend(scissors)
    n-=1
  return rps_helper(n,rock_list) + rps_helper(n,paper_list) + rps_helper(n,scissor_list)
print(rock_paper_scissors(3))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')