'''
Nombre: Gerson Jhair Vasquez Inga
'''

#Pregunta 1:

print("****PREGUNTA 1****")

print("Menu de opciones")
print("1-Dibujar un cuadrado")
print("2-Multiplos de 2")
print("3-Mayores de edad")
print("0-Salir")
opcion=int(input("Ingrese una opcion: "))
while(opcion!=0):
    if opcion==1:
        num_lados=int(input("Ingrese el numero de lados: "))
        for i in range(1,num_lados+1):
            for j in range(1,num_lados+1):
                print("*",end="")
            print("")

    elif opcion==2:
        numElementos = int(input("Numero de elementos de la lista: "))
        listaNum =[]
        for k in range(1,numElementos+1):
            print("Numero ",k,": ")
            numeroAdd = int(input(""))
            listaNum.append(numeroAdd)
        print(listaNum)

        for l in range(0,numElementos):
            if listaNum[l]%2==0:
                print(listaNum[l],"es un multiplo de 2")

    elif opcion==3:
        numPersonas = int(input("Numero de personas: "))
        listaPersonas=[]
        for i in range(1,numPersonas+1):
            nombreEdad=[]
            nombreEdad.clear()
            print("Nombre de persona ",i,": ")
            nombrePersonas=input("")
            print("Edad de persona ",i,": ")
            edadPersonas=int(input(""))
            nombreEdad.append(nombrePersonas)
            nombreEdad.append(edadPersonas)
            listaPersonas.append(nombreEdad)
    
        print("Mayores de edad: ")
        for m in range(0,len(listaPersonas)):
            if listaPersonas[m][1]>=18:
                print(listaPersonas[m][0],"-",listaPersonas[m][1]," años ")

    opcion=int(input("Ingrese una opcion del menu: "))


#Problema 2

print("****PREGUNTA 2*****")

biblioteca ={
    'libros':{
    'La ciudad y los perros':'Mario Vargas Llosa',
    'Cien años de soledad':'Gabriel Garcia Marquez',
    'La Metamorfosis':'Franz Kafka',
    'Poemas humanos':'Cesar Vallejo',
    'Romeo y Julieta':'William Shakespeare'
    },
    'categorias':['comedia','tragedia','novela','drama'],
    'usuarios':['Javier','Juan','Gereny','Andres'],
    'estado':['usado','usado','usado','usado']
}

print("Categorias de los libros: ")
print(biblioteca['categorias'])

print("Libros:")
print(biblioteca['libros'].keys())
print("Autores de libros:")
print(biblioteca['libros'].values())

print("Usuarios de la biblioteca: ")
print(biblioteca['usuarios'])

print("Actualizar el estado de libros")
for i in range(1,5):
    print("Estado de libro ",i)
    biblioteca['estado'][i-1]=input("")
    print(biblioteca['estado'][i-1])
for i in range(1,5):
    print("Estado actual de libro ",i)
    print(biblioteca['estado'][i-1])


#Pregunta 3

print("*****PREGUNTA 3*****")

def numMayor(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2

numero1=input("Ingrese el primer numero: ")
numero2=input("Ingrese el segundo numero: ")
print("El numero mayor es: ",numMayor(numero1,numero2))


#Pregunta 4

print("****PREGUNTA 4****")

import sys
argumentos=sys.argv
print(type(argumentos))

def leerArgumentos(*args):
    for arg in args:
        print(arg)
leerArgumentos(*argumentos)
