class alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = int(nota)
        print("Alumno creado con exito")
    def calificacion(self):
        if self.nota >= 5:
            print("El alumno", self.nombre, "ha aprobado")
        else:
            print("El alumno", self.nombre, "ha suspendido")