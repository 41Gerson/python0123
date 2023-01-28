import os
from main import recursividadProb5
from main import divisionProb5
sumanumeros = int(input("Sumar hasta que numero: "))
numero1=int(input("Ingrese el numerador: "))
numero2=int(input("Ingrese el denominador: "))

try:
    recursividadProb5(sumanumeros)
except:
    print("Hubo un error")
else:
    os.getcwd()
finally:
    print("Proceso de iteracion terminada")



try:
    divisionProb5(numero1,numero2)
except ZeroDivisionError as e:
    print(e)
else:
    os.getcwd()
finally:
    print("Proceso de division terminado")
