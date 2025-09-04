#1. Lee el siguiente código y explica qué hace:
contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
 print("Contraseña incorrecta. Intenta de nuevo.") 
#El código solicita al usuario que ingrese una contraseña y la compara con una contraseña predefinida ("programacion1"). Si la contraseña ingresada coincide con la correcta, muestra un mensaje de bienvenida; de lo contrario, indica que la contraseña es incorrecta y pide que se intente nuevamente.
#¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
#El programa considera las mayúsculas y minúsculas, por lo que si el usuario ingresa la contraseña con mayúsculas (por ejemplo, "Programacion1" o "PROGRAMACION1"), el programa la considerará incorrecta y mostrará el mensaje "Contraseña incorrecta. Intenta de nuevo."
#¿Cómo mejorarías el programa para dar más intentos?
#Ocultaría la contraseña y daria un numero limitado de intentos.


#2.1. Solicita una letra al usuario.
#2.2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra ingresada es una vocal".
#2.3. En otro caso, imprime: "La letra ingresada no es una vocal".
letra=input("Ingrese una letra: ")
if letra in "aeiouAEIOU":
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")
    
#• ¿Cómo manejarías vocales acentuadas (á, é)?
#Las incluiría en la cadena de comparación, por ejemplo: if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
#• ¿Qué estructura usarías para simplificar las comparaciones?
#Dejaria la estrucutura que usé.


#ACTIVIDAD 3
#1. Pide un número al usuario.
#2. Si es positivo, imprime: "El número es positivo".
#3. Si es negativo, imprime: "El número es negativo".
#4. Si es cero, imprime: "El número es cero".
num=float(input("Ingrese un numero: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")
    
#• ¿Qué ocurre si el usuario ingresa un texto?
#El programa lanzará un error de tipo ValueError, ya que no podrá convertir el texto a un número flotante.
#• ¿Cómo adaptarías el código para números decimales?
#Permito el ingreso de numeros flotantes (float).


#ACTIVIDAD 4:
#1. Solicita dos números al usuario.
#2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
#3. Si el primero es menor, imprime: "El primer número ingresado es menor".
#4. Si son iguales, imprime: "Los números ingresados son iguales".
num1=int(input("Ingrese el perimer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print("El primer número ingresado es mayor")
elif num1 < num2:
    print("El primer número ingresado es menor")    
else:
    print("Los números ingresados son iguales")
    
#• ¿Cómo modificarías el programa para comparar más de dos números?
#Usaria listas y la funcion max() o min() para encontrar al numero mayor y al numero menor.
#• ¿Qué pasa si se ingresan valores no numéricos?
#El programa lanzará un error de tipo ValueError, ya que no podrá convertir el texto a un número entero.

#EJERICICIO 5:
#1. Pide la temperatura actual en °C.
#2. Si es ≤ 10°C, imprime: "Hace frío".
#3. Si está entre 10°C y 25°C, imprime: "Está templado".
#4. Si es > 25°C, imprime: "Hace calor".
temp=float(input("Ingrese la temperatura actual en °C: "))
if temp <= 10:
    print("Hace frío")
elif temp > 10 and temp <= 25:
    print("Está templado.")
else:
    print("Hace calor")

#• ¿Cómo adaptarías el programa para usar °F?
#Usaria la formula de conversion: (°C * 9/5) + 32 = °F
#• ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
temp=float(input("Ingrese la temperatura actual en °C: "))
if temp < 0:
    print("Hace mucho frío")
elif temp >= 0 and temp <= 10:
    print("Hace frío")
elif temp > 10 and temp <= 25:
    print("Está templado.")
else:
    print("Hace calor")
    
#ACTIVIDAD 6:
#1. Pide un año al usuario.
#2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se
#ingresó un año bisiesto".
#3. En otro caso, imprime: "Se ingresó un año no bisiesto".
año=int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Se ingresó un año bisiesto")
else:
    print("Se ingresó un año no bisiesto")
    
#• ¿Por qué el año 1900 no es bisiesto?
# Porque es divisible por 100 pero no por 400.
#• ¿Cómo validarías que el año sea positivo?    
# Agregaria una condicion para verificar que el año sea mayor que 0.

#ACTIVIDAD 7:
#1. Pide una frase o palabra al usuario.
#2. Si no termina en punto, añádelo al final.
#3. Imprime el resultado.
frase=input("Ingrese una frase o palabra:")
if frase [-1] != ".":
    print(frase + ".")
else:
    print(frase)

#• ¿Cómo manejarías frases que terminan con espacios?
# Usaria el metodo strip() para eliminar los espacios al final de la frase antes de verificar si termina en punto.
#• ¿Qué otros caracteres de puntuación podrías considerar?
# Podría considerar signos de exclamación (!), signos de interrogación (?), comas (,), puntos y comas (;), entre otros.

#ACTIVIDAD 8:
#1. Pide al usuario que cree una contraseña.
#2. Verifica que cumpla:
#o 8+ caracteres y ≤20 caracteres.
#o Al menos 1 mayúscula (usa .isupper()).
#o Al menos 1 número (usa .isdigit()).
#3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
#4. Si no, imprime: "La contraseña no es segura.".

contra=input("Ingrese una contraseña: ")
if len(contra) > 8 and len(contra) <= 20 and any(c.isupper() for c in contra) and any(c.isdigit() for c in contra):
    print("¡Felicitaciones! Creaste tu contraseña.")
else: 
    print("La contraseña no es segura.") 
    
#• ¿Cómo añadirías la regla de usar un carácter especial?
# Usaria la funcion any() junto con una lista de caracteres especiales para verificar si al menos uno de ellos está presente en la contraseña.  
#• ¿Por qué es importante limitar la longitud máxima?
# Limitar la longitud máxima de una contraseña es importante para evitar que sea demasiado larga, lo que podría dificultar su manejo y almacenamiento seguro. Además, las contraseñas extremadamente largas pueden ser más susceptibles a ciertos tipos de ataques.


#ACTIVIDAD 9:
#1. Basado en el Ejercicio 8, mejora los mensajes de error:
# Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al menos 8 caracteres.".
# Si tiene >20 caracteres: "...no más de 20 caracteres.".
# Si falta mayúscula: "...al menos una mayúscula.".
# Si falta número: "...al menos un número.".
contra=input("Ingrese una contraseña: ")
if len(contra) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif len(contra) > 20:
    print("La contraseña no es segura. Debe tener no más de 20 caracteres.")
elif not any(c.isupper() for c in contra):
    print("La contraseña no es segura. Debe tener al menos una mayúscula.")
elif not any(c.isdigit() for c in contra):
    print("La contraseña no es segura. Debe tener al menos un número.")
else:
    print("¡Felicitaciones! Creaste tu contraseña.")
    
#• ¿Cómo evitarías repetir código al verificar cada condición?
# Usaria una lista para almacenar los mensajes de error y luego imprimirlos todos juntos al final si hay errores.
#• ¿Qué ventajas tiene este enfoque para el usuario?
# Este enfoque proporciona retroalimentación específica sobre qué aspectos de la contraseña no cumplen con los requisitos, lo que ayuda al usuario a corregirlos de manera más eficiente en lugar de recibir un mensaje genérico de error.

#ACTIVIDAD 10: PIEDRA, PAPEL, TIJERAS:+
#1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
#2. Usa la tabla proporcionada para determinar el resultado (ganador o
#empate).

jugador1=input("Jugador 1, ingrese su jugada (piedra, papel o tijera): ").lower()
jugador2=input("Jugador 2, ingrese su jugada (piedra, papel o tijera): ").lower()

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Jugador 1 gana")
elif jugador1==jugador2:
    print("Empate")
else:
    print("Jugador 2 gana")
    
#• ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
#  Si la entrada no es válida, mostraría un mensaje de error y pediría al usuario que ingrese nuevamente.
#• ¿Qué estructura usarías para simplificar las comparaciones?
# Usaria un diccionario para mapear las jugadas y sus resultados, lo que simplificaría la lógica de comparación.