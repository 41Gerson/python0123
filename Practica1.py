'''
Alumno: Gerson Jhair Vasquez Inga
'''

'''
Pregunta 1
Realizar un programa que ingrese sus datos personales e imprimirlos
'''
print("PREGUNTA 1")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dni = input("Ingrese su numero de DNI: ")
num_celular = input("Ingrese su numero de celular: ")
est_civil = input("Ingrese su estado civil: ")
correo = input("Ingrese su correo personal: ")

print("**DATOS PERSONALES**")
print("Nombre: "+nombre)
print("Apellido: "+apellido)
print("DNI: "+dni)
print("Celular: "+num_celular)
print("Estado civil: "+est_civil)
print("Correo: "+correo)



'''
Pregunta 2
Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el
teclado.
'''
print("PREGUNTA 2")
radio = float(input("Ingrese el radio del circulo: "))
lado_triangulo = float(input("Ingrese el lado del triangulo: "))
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))

import math
area_circulo = round(math.pi*pow(radio,2),2)
area_triangulo = round(pow(3,1/2)*pow(lado_triangulo,2)/4,2)
area_cuadrado = round(lado_cuadrado*lado_cuadrado,2)

print(f"Area del circulo: {area_circulo} u2")
print(f"Area del triangulo: {area_triangulo} u2")
print(f"Area del cuadrado: {area_cuadrado} u2")

'''
Pregunta 3
Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división
y división entera.
'''
print("PREGUNTA 3")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))


print("Suma v1+v2: ",valor1+valor2)
print("Suma v2+v3: ",valor2+valor3)
print("Suma v3+v1: ",valor3+valor1)
print("Suma total: ",valor1+valor2+valor3)

print("Resta v1-v2: ",valor1-valor2)
print("Resta v2-v3: ",valor2-valor3)
print("Resta v3-v1: ",valor3-valor1)

print("Multiplicacion v1-v2: ",valor1*valor2 )
print("Multiplicacion v2-v3: ",valor2*valor3 )
print("Multiplicacion v3-v1: ",valor3*valor1 )
print("Multiplicacion v1-v2-v3: ",valor1*valor2*valor3 )

print("Division v1/v2: ",valor1/valor2)
print("Division v2/v3: ",valor2/valor3)
print("Division v3/v1: ",valor3/valor1)

print("Division entera v1-v2: ",valor1//valor2)
print("Division entera v2-v3: ",valor2//valor3)
print("Division entera v3-v1: ",valor3//valor1)

'''
Pregunta 4
Ingrese un valor e imprima el tipo de dato
'''
print("PREGUNTA 4")
tipo = input("Ingrese un valor: ")
print(type(tipo))

'''
Pregunta 5  
Realice un programa que imprima la ubicación de su carpeta donde se encuentra
trabajando.
'''
print("PREGUNTA 5")
import sys
variable =sys.argv[0]
print("Ubicacion del archivo",variable)

'''
Pregunta 6 
Realice un programa que calcule la suma de los números hasta el valor ingresado.
'''
print("PREGUNTA 6")
numero = int(input("Ingrese un numero: "))
suma_numeros = 0
for i in range(1,numero+1):
    suma_numeros = suma_numeros+i
print("La suma total del ","1"," al ",numero,"es: ",suma_numeros)

'''
Pregunta 7 
Realiza un programa que lea 2 números por teclado 
'''
print("PREGUNTA 7")
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))
if num1==num2:
    print("Los numeros son iguales")
else:
    print("Los numeros no son iguales")
    if num1>num2:
        print("El primer numero es mayor")
    elif num2>num1:
        print("El segundo numero es mayor")

'''
Pregunta 8
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas.
'''
print("PREGUNTA 8")
contrasenia1 = input("Ingrese una contraseña: ")
contrasenia2 = input("Ingrese la contraseña: ")
if contrasenia1==contrasenia2:
    print("Coincide")
else:
    print("No coincide")
