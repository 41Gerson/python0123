class Producto:
    def __init__(self,pais,lote,año):
        self.pais=pais
        self.lote=lote
        self.año=año
    def __str__(self) -> str:
        return f"Codigo: {self.pais}-{self.lote}-{self.año} "


pais=input("Pais: ")
lote=input("Numero de lote: ")
año = input("Año de fabricacion: ")
x=Producto(pais,lote,año)
y=x.__str__()
print(y)