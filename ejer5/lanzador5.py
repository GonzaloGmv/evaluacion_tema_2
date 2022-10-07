from ejer5.ejr5 import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta

def main5():
    c = Coche("azul", 4, 150, 1200)
    ca = Camioneta("negro", 4, 120, 1000, 1200)
    b = Bicicleta("blanco", 2, "deportiva")
    m = Motocicleta("rojo", 2, "urbana", 160, 500)
    print(c)
    print(ca)
    print(b)
    print(m)