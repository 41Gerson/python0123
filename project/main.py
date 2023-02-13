


import controller as ctr

import sqlite3

conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()


#Usuarios
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE USUARIOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25),
            PASSWORD VARCHAR(255) NOT NULL,
            EMAIL VARCHAR(255) NOT NULL,
            FULLNAME VARCHAR(25) NOT NULL,
            SCORE INT,
            TIPOUSUARIO VARCHAR(25)
        ); """
cursor_obj.execute(table)

#Productos
cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
table = """ CREATE TABLE PRODUCTOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMEPRODUCT VARCHAR(255) NOT NULL,
            PRICE VARCHAR(20) NOT NULL, 
            CATEGORIA VARCHAR(25) NOT NULL,
            STCOKACTUAL INT,
            CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)

#Venta
cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

table=""" CREATE TABLE VENTA (
            ORDERID  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT, 
            PRICETOTAL VARCHAR(25) NOT NULL
        ); """

cursor_obj.execute(table)

#Inventario
cursor_obj.execute("DROP TABLE IF EXISTS INVENTARIO")

table=""" CREATE TABLE INVENTARIO (
            IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT NOT NULL, 
            CANTIDAD INT NOT NULL,
            FECHA_MOVIMIENTO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)


print("1)Usuarios\n2)Productos\n3)Venta")
option1=input('Ingrese una categoria: ')



if(option1=='1'):
    print("***CATEGORIA USUARIOS***")
    print("1)Insertar\n2)Ver Lista\n3)Buscar")
    option2=input("Ingrese una opcion: ")
    if(option2=='1'):
        def registerUser():
            usuario = input('Ingrese el siguiente data usuario: ')
            password = input('Ingrese el siguiente data password: ')
            email = input('Ingrese el siguiente data email: ')
            fullname = input('Ingrese el siguiente data fullname: ')
            tipousuario = input('Ingrese el siguiente data tipo-usuario: ')
            '''
            data = (usuario, password, email, fullname, tipousuario)
            '''
            try:
                insert = "INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME, ,TIPOUSUARIO) VALUES(?,?,?,?);"
                data = (usuario, password, email, fullname, tipousuario)
                conn.execute(insert, data)
                conn.commit()
            except Exception as e:
                print("Error al ingresar data")
                print(e)

        if __name__ == '__main__':
            registerUser()
    elif(option2=='2'):
        def listUser():
            data = ctr.controllerUser()
            for row in data:
                print(row)

        if __name__ == '__main__':
            listUser()

elif(option1=='2'):
    print("***CATEGORIA PRODUCTOS***")
    print("1)Insertar\n2)Ver Lista\n3)Buscar")
    option2 = input("Ingrese una opcion: ")
    if (option2 == '1'):
        def registerProd():
            print("Ingrese valores")
            nameProduct = input('Ingrese el nombre del producto: ')
            price = input('Ingrese el PRICE: ')
            categria = input('Ingrese el CATEGORIA: ')
            stock = int(input('Ingrese el STCOKACTUAL: '))
            try:
                insert = "INSERT INTO PRODUCTOS(NAMEPRODUCT,PRICE,CATEGORIA,STCOKACTUAL) VALUES(?,?,?,?);"
                data = (nameProduct, price, categria, stock)
                conn.execute(insert, data)
                conn.commit()
            except Exception as e:
                print("Error al ingresar data")
                print(e)
        if __name__ == '__main__':
            registerProd()
    elif (option2 == '2'):
        def listProd():
            data = ctr.controllerProd()
            for row in data:
                print(row)
        if __name__ == '__main__':
            listProd()
elif(option1=='3'):
    print("***CATEGORIA VENTAS***")
    print("1)Insertar\n2)Ver Lista\n3)Buscar")
    option2 = input("Ingrese una opcion: ")
    if (option2 == '1'):
        def registerVent():
            print("Ingrese valores")
            IDProduct = input('Ingrese el ID del producto: ')
            price = input('Ingrese el PRICE: ')
            try:
                insert = "INSERT INTO VENTAS(PRODUCTID,PRICETOTAL) VALUES(?,?,?,?);"
                data = (IDProduct,price)
                conn.execute(insert, data)
                conn.commit()
            except Exception as e:
                print("Error al ingresar data")
                print(e)
        if __name__ == '__main__':
            registerVent()
    elif (option2 == '2'):
        def listVent():
            data = ctr.controllerUser()
            for row in data:
                print(row)
        if __name__ == '__main__':
            listVent()






