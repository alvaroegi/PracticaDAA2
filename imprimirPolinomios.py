def imprimirPolinomios(lista,it):
    lon = len(lista)
    if lon == 1:
        if(lista[-1]) > 0:
            return " + " + str(abs(lista[-1]))
        elif(lista[-1] < 0):
            return " - " + str(abs(lista[-1]))
        elif (it == 0):
            return " + 0"
        else:
            return ""
    else:
        it = it + 1
        if(lista[-1] > 0):
            return " + " + str(abs(lista[-1])) + "x^" + str(lon-1) + imprimirPolinomios(lista[:-1],it)
        elif(lista[-1] < 0):
            return " - " + str(abs(lista[-1])) + "x^" + str(lon-1) + imprimirPolinomios(lista[:-1],it)
        else:
            return imprimirPolinomios(lista[:-1],it)




def casoDePrueba():
    try:
        grado = int(input())
        if(grado >= 0 and grado <= 100):
            numeros = input().split()
            lista = list(map(int, numeros))
            if(len(lista) == (grado+1)):
                if(len(lista) > 1 and lista[-1] != 0) or (len(lista) == 1):
                    print(imprimirPolinomios(lista,0))
                    return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass
