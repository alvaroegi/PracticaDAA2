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

def karatsuba(P, Q, grado):
    """Función para multiplicar dos polinomios utilizando el algoritmo de Karatsuba"""
    m = len(P)
    n = len(Q)
    if m < n:
        P, Q = Q, P
        m, n = n, m
    if n == 0:
        return [0]
    if m <= grado:
        return multPol(P, Q)

    medio = m // 2
    P_a = P[:medio]
    P_b = P[medio:]
    Q_b = Q[:min(n, medio)]
    Q_a = Q[min(n, medio):]
    AC = karatsuba(P_a, Q_b, grado)
    BD = karatsuba(P_b, Q_a, grado)
    A_B = sumaPol(P_a, P_b)
    C_D = sumaPol(Q_b, Q_a)
    AD_BC = restaPol(karatsuba(A_B, C_D, grado), AC)

    #multiplicar por xm
    res = []
    res.extend([0] * (2 * (m - medio)))
    res[:len(AC)] = AC
    for i in range(len(AD_BC)):
        res[medio + i] += AD_BC[i]
    for i in range(len(BD)):
        res[2*medio + i] += BD[i]
    return res

def multPol(P, Q):
    """Función para multiplicar dos polinomios utilizando el método convencional"""
    m = len(P)
    n = len(Q)
    R = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            R[i+j] += P[i] * Q[j]
    return R


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
                                if (len(lista2) == 1 and lista2[0] == 0) or (len(lista) == 1 and lista[0] == 0):
                                    print(" + 0")
                                else:
                                    print(imprimirPolinomios(karatsuba(lista,lista2, len(lista) + len(lista2)),0))
                                return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass