class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con exito")
    def __str__(self):
        return "{}: codigo: {}, precio: {}, tipo: {}".format(self.nombre, self.codigo, self.precio, self.tipo)

patatas = Producto(768, "Patatas", 1.5, "pequeñas")
print(patatas)
patatas.precio = 1.8
print(patatas)