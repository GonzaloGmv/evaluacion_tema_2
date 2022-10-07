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

German = alumno("German", 0)
Carlos = alumno("Carlos", "5")
Zazo = alumno("Zazo", 2)
Migui = alumno("Migui", 0.5)
Moyis = alumno("Moyis", 10)
Gonzalo = alumno("Gonzalo", 6.1)

German.calificacion()
Carlos.calificacion()
Zazo.calificacion()
Migui.calificacion()
Moyis.calificacion()
Gonzalo.calificacion()
