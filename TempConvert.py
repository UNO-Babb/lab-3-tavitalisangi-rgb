#TempConvert.py
#Name:Tavita Afata
#Date:14 Sep 2025
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = int(input("Enter a temperature to convert: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  
  tempC = (tempF -32)* 5//9 
  tempC= round(tempC,2)

  print(tempC)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
