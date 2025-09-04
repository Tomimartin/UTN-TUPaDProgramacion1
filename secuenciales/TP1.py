#EJERCICIO 1
print("Hola Mundo!")

#EJERCICIO 2

nombre=(input("Ingrese su nombre: "))
print(f"¡Hola {nombre}! ")

#EJERCICIO 3

nombre=(input("Ingrese su nombre: "))
apellido=(input("Ingrese su apellido: "))
lugar=(input("Ingrese su lugar de residencia: "))
edad=int(input("Ingrese su edad: "))
print(f"Soy {nombre} {apellido}, soy de {lugar} y tengo {edad} años")

#EJERCICIO 4
import math

radio=float(input("Ingrese el radio del circulo: "))
area= math.pi *radio**2
perimetro= 2*math.pi*radio

print("El valor del área es de: ",area)
print("El valor del perímetro es de: ",perimetro)

#EJERCICIO 5

segundos=int(input("Ingrese una cantidad de segundos: "))
hora=segundos/3600
print(f"{segundos} segundos equivales a {hora} horas.")

#EJERCICIO 6

num=int(input("Ingrese un número: "))

for i in range(1,11):
 print(f"{num} x {i} = {num*i}")
 

#EJERICIO 7

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

suma=num1 + num2
resta=num1-num2
multi=num1*num2
divi=num1/num2

print(f"{num1} + {num2} = ",suma)
print(f"{num1} - {num2} = ",resta)
print(f"{num1} * {num2} = ",multi)
print(f"{num1} / {num2} = ",divi)

#EJERCICIO 8

altura=float(input("Ingrese su altura en metros: "))
peso=float(input("Ingrese su peso en kg: "))
imc= peso/(altura)**2
print("Su indice de masa corporal es de: ",round (imc,2))

#EJERCICIO 9

grados_c=float(input("Ingrese la temperatura en celsius: "))
grados_f=((9/5)*grados_c) + 32

print("La temperatura {grados_c} grados celsius equivales a: ",round (grados_f,2), "Fahrenheit")

#EJERCICIO 10

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

promedio=(num1+num2+num3)/3

print("El promedio de los 3 numeros es de: ",promedio)












