def excepciones():
    try:
        numero = 7/0
    except ZeroDivisionError:
        print("No puedes dividir entre 0")

    try:
        lista = [4, 7, 30, 23, 5]
        lista[10]
    except IndexError:
        print("No puedes llamar al elemento 10 en la lista lista porque no hay tantos elementos")

    try:
        paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
        paises["alemania"]
    except KeyError:
        print("Alemania no pertenece al diccionario paises")

    try:
        resultado = "2" + 10
    except TypeError:
        print("No puedes sumar un string y un entero, el 2 tiene comillas, lo que lo convierte en un string")