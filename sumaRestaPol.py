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

def sumaPol(pol1,pol2):
    lon1 = len(pol1)
    lon2 = len(pol2)
    if lon1 == 0:
        return pol2
    elif lon2 == 0:
        return pol1
    else:
        return [pol1[0] + pol2[0]] + sumaPol(pol1[1:lon1], pol2[1:lon2])

def restaPol(pol1,pol2):
    lon1 = len(pol1)
    lon2 = len(pol2)
    if lon1 == 0:
        for i in range(lon2):
            pol2[i] = -pol2[i]
        return pol2
    elif lon2 == 0:
        return pol1
    else:
        return [pol1[0] - pol2[0]] + restaPol(pol1[1:lon1], pol2[1:lon2])


def casoDePrueba():
    try:
        grado = int(input())
        if(grado >= 0 and grado <= 100):
            numeros = input().split()
            lista = list(map(int, numeros))
            if(len(lista) == (grado+1)):
                if(len(lista) > 1 and lista[-1] != 0) or (len(lista) == 1):
                    grado2 = int(input())
                    if (grado2 >= 0 and grado2 <= 100):
                        numeros2 = input().split()
                        lista2 = list(map(int, numeros2))
                        if (len(lista2) == (grado2 + 1)):
                            if (len(lista2) > 1 and lista2[-1] != 0) or (len(lista2) == 1):
                                print(imprimirPolinomios(sumaPol(lista,lista2),0))
                                print(imprimirPolinomios(restaPol(lista, lista2), 0))
                                return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass
