#este es un archivo de python
#Universidad del Valle de Guatemala
#Ejercicios lab 4 de diseño
import IMC as I
entrada = 0
peso = 0
altura = 0
IMC = 0
prog = 0
while (prog != 6):
    print("1.Ejercicio del IMC")
    print("2.Ejercicio de comparar valores distintos")
    print("3.Ejercicio de comparar tres valores distintos")
    print("4.Ejercicio de sumatoria de numeros enteros")
    print("5.Ejercicio de notas de 5 alumnos que han ganado la clase")
    print("6.Salir")
    prog = int(input("Ingrese el ejercicio que desea ver: "))
    if prog == 1:
        while (entrada != 3):
            print("1.Calcular el IMC")
            print("2.Ver mi rango")
            print("3.Salir")
            entrada = int(input("Ingrese el numero de lo que desea "))
            if (entrada == 1):
                peso = float(input("ingrese su peso en Kg: "))
                altura = float(input("Ingrese su estatura en metros: "))
                print("El IMC es " + str(I.Indice(peso,altura)))
            elif (entrada == 2):
                try:
                    print(I.Compare(I.Indice(peso,altura)))
                except:
                    print("Debe de ingresar primero su IMC")
