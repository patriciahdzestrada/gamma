def funcion():
    numeros = [12, 45, 7, 89, 23, 56]
    mayor=numeros[0]
    for i in numeros:
        if i < mayor:
            mayor
        else:
            mayor=i
    return mayor