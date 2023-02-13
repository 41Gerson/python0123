print("Hola mundo\nholaaa")
print("mi nombre es Gerson")
numero1 = 10
print(numero1)
print(type(numero1))
numero2 = 15.23
print(numero2)
print(type(numero2))
cadena1 = "Gerson"
print(cadena1)
print(type(cadena1))
cadena2 = "Estoy 'estudiando'"
print(cadena2)
print(type(cadena2))
valor1 = False
print(valor1)
print(type(valor1))
valor2 = True
print(valor2)
print(type(valor2))
num1 = 12
num2 = 13
suma = num1+num2*10
print(suma)
print("El resultado es: ",suma)
valor3 = 20
print(valor3)
valor3 = "Gerson"
print(valor3)
#Este es un comentario
'''
    Este es un comentario 
    donde puedo escribir 
    mas de uan linea,poner 
    3 comillas simples
'''
palabra = "Python"
print(palabra[1:6:2])
#Cada palabra se cuenta de 0,1,2,3...

palabra2 = "gerson"
print(palabra2.capitalize())
#Primer caracter en mayuscula el resto en minuscula

cadena = "Estoy 'estudiando'"
print(cadena)
#Una forma de imprimir comillas
#se puede intercalar ' y "

cad = "Estoy \"estudiando\""
print(cad)
#Forma de imprimir el mismo tidp de comilla "

cade = r"D:\nombre\trabajos"
print(cade)
#Imprime sin la funcion de los "\"

print("""Hola soy aaaaa
fer
egdsfy
er""")
#Cadena mas larga en muchas lineas

caden = 'hola mundo'.upper()
#Combierte toda la cadena a mayuscula
print(caden)
#otra forma
#print(caden.upper())

#lo contrario, minuscula es lower()
#title() mayucula las primeras letras de las palabras
#count('x') cuenta la letra-palabra 'x' en la cadena
#.isdigit() te dice si todos los digitos son numeros (True)
#.isalpha() te dice si todos los digitos son letras (True)
#.isalnum() te dice si tofos los digitos son letras y numeros (true)


cadena3 = " xx ".join(("marciano"))
print(cadena3)
#Separa cada digito de la cadena por " *lo que pongas"

cadena4 = "   hola    ".strip()
print(cadena4)
#Quita el digito que se ponga en () si esta vacio te quita los espacios




#VARIABLES

valora = 10
valorb = 3
resultado1 = valora + valorb
resultado2 = valora - valorb
resultado3 = valora * valorb
resultado4 = valora/valorb
resultado5 = valora//valorb
#dos slash da el valor exacto de division
resultado6 = valora % valorb
#da el residuo
resultado7 = valora ** valorb
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)

prueba1 = 10 < 20
prueba2 = 10 > 20
prueba3 = 10 == 20
'''
ese doble igual es para comparar
un igual es para asignar
'''
prueba4 = 10 != 20
print(prueba1)
print(prueba2)
print(prueba3)
print(prueba4)

'''
Prioridad de op logicos
NOT
AND
OR
'''
ejemplo = ((10>12)or(10<13)and(10==13)or(10>=12))
print(ejemplo)

'''
Prioridad de op generales
()
**
* / mod not
+ - and
> < == >= <= != or
'''

a = 0
#Primero declarar una variable
a = a + 5
# tambien +=,-=,*=,/=
a -= 2
a **=2
#elevado al cuadrado
a %=2
#modulo de asignacion
print(a)

# Salidas
nombre = 'Gerson'
edad = 21
print("hola",nombre,"tienes",edad,"años")


print("hola {} tienes {} años".format(nombre,edad))
print(f"Hola {nombre} tienes  {edad} años")

'''

#Entrada de datos
nombre1 = input("Digite su nombre: ")
#input para datos cadena
print(f"Hola {nombre1}")
#Se puede digitar una cadena con espacios

numero3 = int(input("Digite un numero: "))
#Para numeros poner int(enteros) o float(flotantes)
print(f"El numero es {numero3 +1}")

'''
#Funciones integradas
n1 = float("10.8")
print(n1)

n2 = str(10.98)
print(n2)

n3 = bin(10)
print(n3)
#Numeros binarios

n4 = hex(10)
print(n4)
#Numeros hexagesimal

n5 = int("0b1010",2)
print(n5)

n6 = abs(-8)
print(n6)

n7 = round(5.6)
print(n7)
#Redondear

n8 = len("Gerson")
print(n8)
#Cuenta los caracteres de la cadena


'''
#Ejercicio 1
avalor = float(input("Digite el valor de a: "))
bvalor = float(input("Digite el valor de b: "))
cvalor = float(input("Digite el valor de c: "))
resp = ((avalor**3)*(bvalor**2-2*avalor*cvalor))/(2*bvalor)
print(f"La respuesta es: {resp}")

#Ejercicio 2
va = float(input("Digite el valor a: "))
vb = float(input("Digite el valor b: "))
solog = ((3+5*8)<3 and ((-6/3 * 4)+2<2)) or (va>vb)
print(f"La respuesta es: {solog}")

#Ejercicio 3
vva = float(input("Ingrese un numero: "))
vvb = float(input("Ingrese otro numero: "))
vvc = vva
vva = vvb
vvb = vvc
print(f"El primer numero es {vva}")
print(f"El segundo numero es {vvb}")

 Otra solucion
 vva , vvb = vvb , vva
 asi se intercambian valores


#Ejercicio 4
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1415
area = pi * radio**2
longitud = 2 * pi * radio
print(f"El area es {area}")
print(f"La longitud es {longitud}")
print(f"El area es {area:.2f}")
#indica que solo se quiere 2 decimales

Otra forma
colocar:
import math
radio -.........
area = math.pi * radio**2
ese "math.pi" es el valor automatico de pi


#Ejercicio 5
pago = float(input("Ingrese el pago de su compra: "))
descuento = 15*pago/100
print(f"El pago final es {pago-descuento}")
'''

'''
#Condicionales
num = int(input("Digite un numero: "))
if 0<num<100:
    print("El numero es positivo")
elif num == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")
print("Fin del programa")
'''


#Ejercicio 1 condicionales
'''
nu1 = int(input("Digite un numero: "))
nu2 = int(input("Digite otro numero: "))

if nu1%2==0 and nu2%2==0:
    print("Ambos son pares")
elif nu1%2==0 and nu2%2!=0:
    print(f"{nu1} es par")
elif nu1%2!=0 and nu2%2==0:
    print(f"{nu2} es par")
else:
    print("Ningun numero es par")
'''


#Ejercicio 2 condicionales
'''
nm1 = int(input("Ingrese el primer numero: "))
nm2 = int(input("Ingrese el segundo numero: "))
nm3 = int(input("Ingrese el tercer numero: "))
if nm1>=nm2 and nm1>=nm3:
    mayor=nm1
elif nm2>=nm1 and nm2>=nm3:
    mayor=nm2
elif nm3>=nm1 and nm3>=nm2:
    mayor=nm3

print(f"El numero mayor es {mayor}")

'''

#Ejericico 3 condicionales
'''
vocal = str(input("Ingrese una vocal: ")).lower()
#Ese lower sirve en caso ingreses la vocal en mayuscula y lo lea como vocal
#Tambien se puede usar el:  .upper()
#otra forma es poner debajo de vocal : vocal.lower()
if vocal=='a' or vocal=='b' or vocal=='c' or vocal=='d' or vocal=='e':
    print(f"{vocal} si es una vocal")
else:
    print(f"{vocal} no es una vocal")
'''

#Ejercicio 4 condicionales
'''
nmr1 = float(input("Ingrese el primer numero: "))
nmr2 = float(input("Ingrese el segundo numero: "))
op = str(input("S,s-Suma\nR,r-Resta\nP,p,M,m-Multiplicacion\nD,d-Division\nIngrese la operacion que desea: "))
op = op.lower()
#Otra manera de validar la letra mayusculas
if op=='s':
    rsp1 = nmr1 + nmr2
    print(f"La respuesta de la operacion es {rsp1} ")
elif op=='r':
    rsp2 = nmr1 - nmr2
    print(f"La respuesta de la operacion es {rsp2} ")
elif op=='p' or op=='m':
    rsp3 = nmr1*nmr2
    print(f"La respuesta de la operacion es {rsp3} ")
elif op=='d':
    rsp4 = nmr1/nmr2
    print(f"La respuesta de la operacion es {rsp4} ")
else:
    print("Esa operacion no existe")
'''

#Ejercicio 5 condicionales
'''
si = 1000
print("Su saldo inicial es de 1000 dolares")
print("1.Ingresar dinero en la cuenta\n2.Retirar dinero de la cuenta\n3.Mostrar dinero disponible\n4.Salir")
operacion = int(input("Ingrese la operacion que desee: "))
if operacion==1:
    ingreso = float(input("Ingrese la cantidad de dinero que desee ingresar: "))
    saldo = si + ingreso
    print(f"Dinero en la cuenta: {saldo}")
elif operacion==2:
    salida = float(input("Ingrese la cantidad de dinero que desee retirar: "))
    if salida>si:
        print("La cantidad de dinero que desea retirar no es posible")
    else:
        saldo = si - salida
        print(f"Dinero en la cuenta: {saldo}")
elif operacion==3:
    saldo = si
    print(f"Su dinero actual es {saldo}")
elif operacion==4:
    print("Salir")
else:
    print("Error")
'''
