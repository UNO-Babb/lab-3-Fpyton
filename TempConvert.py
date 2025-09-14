#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  Celsius = (fahrenheit -32) * 5/9
  Celsius = round(Celsius, 1)
  #Output converted temperature.
  tempF = 80

  tempC = (tempF - 32) * 5/ 9
  print("Temperature in celsius", Celsius)
  
if __name__ == '__main__':
  main()
