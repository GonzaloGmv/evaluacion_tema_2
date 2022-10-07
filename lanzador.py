from ejer1.lanzador1 import main1
from ejer2.lanzador2 import main2
from ejer3.lanzador3 import main3
from ejer4.lanzador4 import main4
from ejer5.lanzador5 import main5

def main():
    while True:
        ejr = input("Escriba el numero del ejercicio que desea iniciar, 1, 2, 3, 4, 5: ")
        try:
            ejr == '1' or ejr == '2' or  ejr == '3' or ejr == '4' or ejr == '5'
        except:
            pass
        else:
            if ejr == '1' or ejr == '2' or  ejr == '3' or ejr == '4' or ejr == '5':
                break
    if ejr == '1':
        main1()
    elif ejr == '2':
        main2()
    elif ejr == '3':
        main3()
    elif ejr == '4':
        main4()
    elif ejr == '5':
        main5()