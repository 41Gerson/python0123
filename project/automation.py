import pandas as pd
import os
import db


print("1)Insertar data:\n2)Actualizar data del dolar")
a=int(input('Ingrese la tarea a realizar: '))

if(a=='1'):
    def insertData():
        #obtiene la ruta absoluta
        path_=os.getcwd()+'\dataTienda.csv'
        #conection a bd
        conn=db.Conection('tienda.db')
        cursor=conn.getCursor()
        print(path_)
        df = pd. read_csv (path_, sep = ";")
        ### logica para insertar
        for i,fila in df.iterrows():
            print(fila['ORDER_ID'])
    if __name__ == '__main__':
        insertData()
elif(a=='2'):
    def updateDolar():
        url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
        pass
        print("Se ha actualizado")
    if __name__ == '__main__':
        updateDolar()