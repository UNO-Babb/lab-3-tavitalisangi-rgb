#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  player = int(input("How many decimal points to compute (0 - 10):"))

  start = time.time()
  
  approxPi = 4/1
  sign = -1
  denom = 3

  while round(approxPi, player) != round(realPi, player):
    approxPi = approxPi + (sign * 4/ denom)

    sign = sign * -1
    denom = denom + 2
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print("Pi:", round(approxPi, player))
  print("Calculated in", elapsedTime, "seconds.")
 

if __name__ == '__main__':
  main()
