exercises = int(input("Enter the number of exercise that need execute"))

if exercises == 17:

  number = float(input("Enter the number: "))

  if number > 0:
    print("The number " + str(number) + " is positive")
  elif number < 0:
    print("The number " + str(number) + " is negative")
  else:
    print("The number " + str(number) + " is neutral")

elif exercises == 18:

  number2 = float(input("Enter the first number: "))
  number = float(input("Enter the second number: "))

  if higher > number:
    print("The higher number is " + str(number2))
  else:
    print("The higher number is " + str(number))

elif exercises == 19:

  first_number = float(input("Enter the first number: "))
  second_number = float(input("Enter the second number: "))
  third_number = float(input("Enter the third number: "))

  if first_number > second_number  > third_number:
    print("The higher number is " + str(first_number) + " and the lower number is " + str(third_number))
  elif first_number > third_number  > second_number:
    print("The higher number is " + str(first_number) + " and the lower number is " + str(second_number))
  elif second_number > first_number > third_number:
    print("The higher number is " + str(second_number) + " and the lower number is " + str(third_number))
  elif second_number > third_number > first_number:
    print("The higher number is " + str(second_number) + " and the lower number is " + str(first_number))
  elif third_number > first_number > second_number:
    print("The higher number is " + str(third_number) + " and the lower number is " + str(second_number))
  else:
    print("The higher number is " + str(third_number) + " and the lower number is " + str(first_number))

elif exercises == 20:

  name = str(input("Enter the name of the employee: "))
  normal_hours = float(input("Enter the number of normal hours worked: "))
  extra_hours = float(input("Enter the number of extra hours worked: "))

  salary = normal_hours*4 + extra_hours*8

  print("The salary of the employee " + name + " is " + str(salary))

elif exercises == 21:

  number_a = float(input("Enter the number A: "))
  number_b = float(input("Enter the number B: "))

  if number_a < number_b:
    print("The addition is " + str(number_a + number_b))
  else:
    print("The subtraction is " + str(number_a - number_b))

elif exercises == 22:

  divider = float(input("Enter the divider: "))
  dividend = float(input("Enter the dividend: "))

  if dividend == 0:
    print("Cannot be divided by 0")
  else:
    print("The result of division is " + str(divider / dividend))

elif exercises == 23:

  number_day = int(input("Enter the number of day: "))

  if number_day == 1:
    print("Monday")
  elif number_day == 2:
    print("Tuesday")
  elif number_day == 3:
    print("Wednesday")
  elif number_day == 4:
    print("Thursday")
  elif number_day == 5:
    print("Friday")
  elif number_day == 6:
    print("Saturday")
  elif number_day == 7:
    print("Sunday")

elif exercises == 24:

  first_side = float(input("Enter the first side: "))
  second_side = float(input("Enter the second side: "))
  third_side = float(input("Enter the third side: "))

  if first_side == second_side == third_side:
    print("The triangle is equilateral")
  else:
    print("The triangle is not equilateral")

elif exercises == 25:

  number_a = float(input("Enter the number A: "))
  number_b = float(input("Enter the number B: "))

  if number_a < 0 or number_b < 0:
    print("The addition is " + str(number_a + number_b))
  else:
    print("The multiplication is " + str(number_a * number_b))

elif exercises == 26:

  day = int(input("Enter the day of your birth: "))
  mont = int(input("Enter the number of mont of your birth: "))

  if (mont == 1 and day >= 20) or (mont == 2 and day <= 18):
    print("Acuario")
  elif (mont == 2 and day >= 19) or (mont == 3 and day <= 20):
    print("Piscis")
  elif (mont == 3 and day >= 21) or (mont == 4 and day <= 19):
    print("Aries")
  elif (mont == 4 and day >= 20) or (mont == 5 and day <= 20):
    print("Tauro")
  elif (mont == 5 and day >= 21) or (mont == 6 and day <= 20):
    print("Géminis")
  elif (mont == 6 and day >= 21) or (mont == 7 and day <= 22):
    print("Cáncer")
  elif (mont == 7 and day >= 23) or (mont == 8 and day <= 22):
    print("Leo")
  elif (mont == 8 and day >= 23) or (mont == 9 and day <= 22):
    print("Virgo")
  elif (mont == 9 and day >= 23) or (mont == 10 and day <= 22):
    print("Libra")
  elif (mont == 10 and day >= 23) or (mont == 11 and day <= 21):
    print("Escorpio")
  elif (mont == 11 and day >= 22) or (mont == 12 and day <= 21):
    print("Sagitario")
  else:
    print("Capricornio")

