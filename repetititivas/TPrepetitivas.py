#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print(i)
    
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num=int(input("Ingrese un numero entero: "))
contador=0
while num != 0:
    num=num//10
    contador+=1 
print("La cantidad de digitos es de: ",contador)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
suma=0
for i in range (num1+1,num2):
    suma+=i

print (f"La suma de los numeros comprendidos entre {num1} y {num2} es de: ",suma)  

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0. 

suma=0
while True:
    num=int(input("Ingrese un numero entero: "))
    if num == 0:
     break
   
suma+=num
   
print("La suma total es de: ",suma) 


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num=random.randint(0,9)
num_adivinar=int(input("Adivine el numero aleatorio entre 0 y 9: "))
intentos=1
while num_adivinar != num:
    intentos+=1
    num=int(input("No es correcto, intente nuevamente: "))
print("Adivinaste el numero!. Tuviste un total de ",intentos," intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range (100-2,0,-2):
    print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
num=int(input("Ingrese un numero: "))
suma=0
for i in range (0,num):
    suma+=i
print ("La suma de los numeros comprendidos entre 0 y ",num," es de: ",suma)
   
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.
contador_num=0
cont_positivos=0
cont_negativos=0
cont_pares=0
cont_impares=0
while contador_num<100:
    num=int(input("Ingrese un numero entero: "))
    if num>0 and num%2==0:
        cont_positivos+=1
        cont_pares+=1
    elif num<0 and num%2==0:
        cont_negativos+=1
        cont_pares+=1
    elif num % 2 != 0 and num<0 :
        cont_impares+=1
        cont_negativos+=1
    elif num % 2 != 0 and num>0:
        cont_impares+=1
        cont_positivos+=1
    else:
        print("EL NUMERO INGRESADO ES 0 O NO ES ENTERO.")

print("El total de numeros pares es de: ",cont_pares)
print("El total de numeros impares es de: ",cont_impares)
print("El total de numeros negativos es de: ",cont_negativos)
print("El total de numeros positivos es de: ",cont_positivos)
    
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores.
suma=0
contador=0
while contador<100:
    num=int(input("Ingrese un numero entero: "))
    suma+=num
    contador+=1
media=suma/100
print("La media de la suma de los numeros enteros es de: ",media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num=int(input("Ingrese el numero a invertir: "))
i=0
while num>0:
    dig=num % 10
    i=(i*10)+dig
    num=int(num/10)
print ("El numero ",num," invertido sería: ",i) 
    
    

    


