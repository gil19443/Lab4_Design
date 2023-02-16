

def Indice (peso, altura):
    IMC = peso/(altura**2)
    return IMC
def Compare (IMC):
    if (IMC < 18.5):
        lect = "Se encuentra en el rango de peso insuficiente"
    elif (IMC >= 18.5 and IMC <= 24.9):
        lect = "Se encuentra en el rango de peso normal"
    elif (IMC >= 25 and IMC <= 29.9):
        lect = "Se encuentra en el rango de sobrepeso"
    else:
        lect = "Se encuentra en el rango de obesidad"
    return lect