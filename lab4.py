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
    elif prog == 2:
        valora = float(input("Ingrese un numero: ")) 
        valorb = float(input("ingrese otro numero: "))
        if (valora > valorb):
            print(f"El valor más grande es {valora}")
        else:
            print(f"El valor más grande es {valorb}")
    elif prog == 3:
        a = float(input("Ingrese un numero: ")) 
        b = float(input("ingrese otro numero: "))
        c = float(input("ingrese otro numero: "))
        lista = [a,b,c]
        print(f"El valor mas grande es {max(lista)}")
        print(f"El valor mas pequeño es {min(lista)}")
    elif prog == 4:
        A = int(input("Ingrese el numero entero para saber la sumatoria consecutiva: "))
        print("La sumatoria es: "+ str((A*(A+1))/2))
    elif prog ==5:
        alums = []
        gan = 0
        for i in range (5):
            alumno = float(input("ingrese la nota del alumno: "))
            if (alumno > 61):
                gan = gan +1
        print("Los que ganaron son: "+str(gan))
        print("Los que perdieron son: "+str(5-gan))
#Estos son cambios de renato
