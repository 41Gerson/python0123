class Productos:
    def __init__(self,nombreProducto,precio,marca,añoFabricacion):
        self.nombreProducto=nombreProducto
        self.precio=precio
        self.marca=marca
        self.añoFabricacion=añoFabricacion
class Catalogo:
    listaProductos=[]
    def __init__(self,listaProductos:list=[]):
        self.listaProductos=listaProductos
    
    def agregar(self,c):
        self.listaProductos.append(c)
    def mostrar(self):
        for i,c in enumerate(self.listaProductos):
            i+=1
            print(i,c)
    
cat=Catalogo()
numProductos=int(input("Numero de productos que existen; "))
for i in range(1,numProductos+1):
    print("Producto ",i)
    nomProd=input("Nombre de producto: ")
    prec=int(input("Precio: "))
    marc=input("Marca: ")
    año=input("Año de fabricacion: ")
    x=Productos(nomProd,prec,marc,año)
    
    cat.agregar(x)

cat.mostrar()





