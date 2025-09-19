#1. Escribir un programa que pida al usuario una palabra y la muestre por
#pantalla 10 veces.
palabra=input("Ingrese la palabra que quiera repetir: ")
for i in range (1,11):
    print(i,".",palabra)
    
#2. Escribir un programa que pregunte al usuario su edad y muestre por
#pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Ingrese su edad: "))
for i in range (1,edad+1):
    print (i, "años.")

#3. Escribir un programa que pida al usuario un número entero y muestre
#por pantalla un triángulo rectángulo como el de más abajo, de altura el
#número introducido.

num=int(input("Ingrese un numero: "))

for i in range (1, num+1):
 print ("*" * i)
 
#4. Escribir un programa que muestre por pantalla la tabla de multiplicar
#del 1 al 10.
resultado=0
for i in range(1,11):
 resultado = i * 10
 print(f"{i} * 10 = ",resultado)
 
#5. Escribir un programa que almacene la cadena de
#caracteres contraseña en una variable, pregunte al usuario por la
#contraseña hasta que introduzca la contraseña correcta
contraseña="123456789"

while True:
    correcta=input("Ingrese la contraseña: ")
    if correcta==contraseña:
     break
    else:
     print("Contraseña incorrecta, intente nuevamente.")
print("CONTRASEÑA CORRECTA!")

#6. Escribir un programa que muestre el eco de todo lo que el usuario
#introduzca hasta que el usuario escriba “salir” que terminará. 

clave="salir"

while True:
    palabra=input("Ingrese una palabra o frase: ")
    if palabra==clave:
        break
    else:
        print(palabra)
        
#7. Escribe un bucle for que imprima los números pares del 2 al 20
#(inclusive). 

for i in range (2,20+2,2):
 print(i)
 
#8. Imprime números del 1 al 100, pero:
#Para múltiplos de 3 → "Fizz".
#Para múltiplos de 5 → "Buzz".
#Para múltiplos de ambos → "FizzBuzz". 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i," FizzBuzz")
    elif i % 3 == 0:
        print(i," Fizz")
    elif i % 5 == 0:
        print(i," Buzz")
    else:
        print(i)

#9. Desarrollar un programa que solicite la carga de 10 números e imprima
#la suma de los últimos 5 valores ingresados.
# Programa que pide 10 números y muestra la suma de los últimos 5

numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma_ultimos = sum(numeros[-5:])

print("La suma de los últimos 5 números es:", suma_ultimos)


#10. Realizar un programa que lea los lados de n triángulos.
#Informar después de cada triángulo si es equilátero (tres lados iguales),
#isósceles (dos lados iguales) o escaleno (ningún lado igual). Informar
#después del total de triángulos de cada tipo.

equilateros = 0
isoceles = 0
escalenos = 0

n = int(input("¿Cuántos triángulos quiere ingresar?: "))

for i in range(1, n+1):
    print(f"\nTriángulo {i}:")
    a = float(input("Ingrese el lado A: "))
    b = float(input("Ingrese el lado B: "))
    c = float(input("Ingrese el lado C: "))

    if a == b == c:
        print("Es equilátero")
        equilateros += 1
    elif a == b or a == c or b == c:
        print("Es isósceles")
        isoceles += 1
    else:
        print("Es escaleno")
        escalenos += 1

print("\n--- RESULTADOS ---")
print("Equiláteros:", equilateros)
print("Isósceles:", isoceles)
print("Escalenos:", escalenos)

    
        
    
     
    

    



