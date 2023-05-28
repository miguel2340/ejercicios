exercises = int(input("Enter the number of exercise that need execute: "))
 
if exercises == 1:

  def multiples_3():
    for i in range(1, 100):
      if i % 3 == 0:
         print(i)

  multiples_3()
elif exercises == 2:
  def imprimir_impares():
    for i in range(0, 100):
      if i % 2 != 0:
       print(i)
  imprimir_impares()
elif exercises == 3:
  def print_pares():
    for i in range(100):
      if i % 2 == 0:
       print(i)
  print_pares()
elif exercises == 4:
  def numero():
      a = 1
      b = 3
      for i in range(a, b + 1):
        print(i)
  numero()
elif exercises == 5:
  def count(max):
    for i in range(max, 0, -1):
      print(i)
    
  count(10)
elif exercises == 6:
  def cuadrado(n):
    return n**2
  for x in range(1, 31):
        print(x, ":", cuadrado(x))
  cuadrado(30)
elif exercises == 7:
  suma = 0
  for _ in range (101):
    print(_**2)
    suma += _**2
  print("La suma es " + str(suma))
elif exercises == 8:
  number = int(input("enter a number: "))
  sum = 0
  for _ in range(number,(number + 101)):
    sum += _
  print(sum)
elif exercises == 9:
  num = int(input("enter a number: "))
  fact=1
  for _ in range(1, num+1):
    fact*=_
  print("the factorial of",num,"is: ",fact)
elif exercises == 10:
  fahrenheit = float(input("temp: "))
  if fahrenheit == 999:
    print("end")
  elif fahrenheit < 999:
    celcius = (5 / 9) * (fahrenheit - 32)
    print(celcius)
elif exercises == 11:
  limit = int(input("number: "))
  for _ in range(2, (limit + 1)):
    primo = True
    for i in range(2, int((sqrt(_))+1)):
      if _ % i == 0:
        primo = False
        break
    if primo:
      print(_)
elif exercises == 12:
  num = int(input("number: "))
  def tabla(n):
    for i in range(1, 11):
        print('{} * {} = {}'.format(n, i, n * i))

  tabla(num)