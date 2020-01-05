import time

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
