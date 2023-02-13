'''
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


'''
'''
# comentamos las insercciones ya que solo sera parte de la creacion de tablas
insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('admin','admin','admin@datux.com','admin datux',0,'admin')"

conn.execute(insert)
insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('cliente','cliente','email','cliente',0,'cliente')"
conn.execute(insert)


print("Table is Ready")

print("Ingrese valores")
nameProduct=input('Ingrese el nombre del producto: ')
price=input('Ingrese el PRICE: ')
categria=input('Ingrese el CATEGORIA: ')
stock=int(input('Ingrese el STCOKACTUAL: '))

insert="INSERT INTO PRODUCTOS(NAMEPRODUCT,PRICE,CATEGORIA,STCOKACTUAL) VALUES(?,?,?,?);"
data=(nameProduct,price,categria,stock)
conn.execute(insert,data)


conn.commit()


'''