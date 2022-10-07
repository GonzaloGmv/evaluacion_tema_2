from ejr3 import Producto

def main3():
    patatas = Producto(768, "Patatas", 1.5, "pequeñas")
    print(patatas)
    patatas.precio = 1.8
    print(patatas)