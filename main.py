import time

def repeat():

  oper = str(input("What operation would you like to do? (+, -, *, /): "))
  time.sleep(1)


  firstDigitques = int(input("What is your first digit?: "))

  secondDigitques = int(input("What is your second digit?: "))




  if oper == "+":
    print('your answer is', firstDigitques + secondDigitques)

  elif oper == "-":
    print('your answer is', firstDigitques - secondDigitques)

  elif oper == "*":
    print('your answer is', firstDigitques * secondDigitques)

  elif oper == "/":
    print('your answer is', firstDigitques / secondDigitques)
  time.sleep(2)
  
  retry =  str(input("Would you like to make another calculation? (y/n)"))

  if retry == "y":
    repeat()
  
  elif retry == "n":
    print("Thank You for using the Math Calculator!")

repeat()
