print ("EJERCICIO 1:CALCULAR EL AREA DE UN TRIANGULO")
base=input("CUAL ES LA BASE: ")
altura=input("CUAL ES LA ALTURA: ")
area=int (base) * int (altura) / 2
print ("el resultado es: " + str (area))
print("EJERCICIO 2:SUMA DE DOS NUMEROS")
n1=float(input("Intro número uno: "))
n2=float(input("Intro numero dos: "))
suma=n1+n2
print("La suma es: ",suma)
print("EJERCICIO 3:ELEVAR UN NUMERO AL CUADRADO")
n3=float(input("numero a potenciar: "))
potencia=n3**2
print("la potencia es: ",potencia)
print("EJERCICIO 4:SUMA DE 1234 MAS 532")
print("1234 + 532")
suma=1234+532
print("resultado de la suma: ",suma)
print("Ejercicio 5:RESTA DE 1234 MENOS 532")
print("1234 - 532")
resta=1234-532
print("resultado de la resta: ",resta)
print("EJERCICIO 6:MULTIPLICACION DE 1234 POR 532")
print("1234 * 532")
x=1234*532
print("resultado de la multiplicacion: ",x)
print("EJERCICIO 7:DIVICION DE 1234 ENTRE 532")
print("1234 / 532")
DIVICION=1234/532
print("resultado de la divicion: ",DIVICION)
print("EJERCICIO 8:MODULO DE 1234 Y 532")
print("1234 % 532")
modulo=1234%532
print("resultado del modulo: ",modulo)
print("EJERCICIO 9:CONVERTIDOR DE EUROS A DOLARES")
euros1=int(input("introduzca euros:"))
dol4=euros1/0.9
print("dolares=", dol4)
print("EJERCICIO 10:AREA DE UN RECTANGULO")
ancho=float(input("Ingrese la ancho del rectangulo:"));
altura=float(input("ingrese la altura del rectangulo:"))
area= (ancho* altura)
print("el area es :", area)
print("EJERCICIO 11:AREA Y PERIMETRO DE UN CUADRADO")
LADO=float(input("INDICA EL LADO DEL CUADRADO: "))
perimetro=LADO*4
area=LADO*LADO
print("el perimetro del cuadrado es: ",perimetro)
print("el area del cuadrado es: ",area)
print("EJERCICIO 12:AREA Y VOLUMEN DE UN CILINDRO")
import os, math
altura = float (input ('Ingresa el valor de altura: '))
radio = float (input ('Ingresa el valor de radio: '))
volumen=math.pi*radio*radio*altura
area=2*math.pi*radio*(radio+altura)
print ('Valor de area: ' + repr (area))
print ('Valor de volumen: ' + repr (volumen))
print("EJERCICIO 13 : LONGITUD Y AREA DE UNA CIRCUNFERENCIA")
radio = float (input ('Ingresa el valor del radio: '))
longitud= 2*3.1416* radio
area= 3.1416*radio**2
print("la longitud del circulo es : ",longitud)
print("el area del circulo es: ",area)
print("EJERCICIO 14: PROMEDIO DE 3 NUMEROS")
a = float (input ('Ingresa el valor de a: '))
b = float (input ('Ingresa el valor de b: '))
c = float (input ('Ingresa el valor de c: '))
promedio=(a+b+c)/3
print("el promedio corresponde a: ",promedio)