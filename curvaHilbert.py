import matplotlib.pyplot as plt

#Siendo: order el orden de la curva,
#x,y: las coordenadas de la esquina inferor izquierda del cuadrado
#size: es la longitud del lado del cuadrado
#orientation: es la orientación de la curva
def curvaHilbert(order, x, y, size, orientation):
    if order == 1:
        #Calculamos los puntos medios de cada cuadrante, coordenada (x,y) y los unimos según su orientación
        point1x = x - size / 2
        point1y = y - size / 2
        point2x = x - size / 2
        point2y = y + size / 2
        point3x = x + size / 2
        point3y = y + size / 2
        point4x = x + size / 2
        point4y = y - size / 2
        if orientation == 1: #Orientanción hacia la derecha
            r1x = [point1x, point4x]
            r1y = [point1y, point4y]
            r2x = [point1x, point2x]
            r2y = [point1y, point2y]
            r3x = [point2x, point3x]
            r3y = [point2y, point3y]
            #almacenamos las tres rectas obtenidas con plot
            plt.plot(r1x, r1y)
            plt.plot(r2x, r2y)
            plt.plot(r3x, r3y)
        elif orientation == 0: #Orientación normal
            r1x = [point1x, point1x]
            r1y = [point1y, point2y]
            r2x = [point1x, point3x]
            r2y = [point1y, point1y]
            r3x = [point3x, point3x]
            r3y = [point1y, point2y]
            plt.plot(r1x, r1y)
            plt.plot(r2x, r2y)
            plt.plot(r3x, r3y)
        elif orientation == -1: #Orientación hacia la izquierda
            r1x = [point1x, point4x]
            r1y = [point1y, point4y]
            r2x = [point3x, point4x]
            r2y = [point3y, point4y]
            r3x = [point2x, point3x]
            r3y = [point3y, point3y]
            plt.plot(r1x, r1y)
            plt.plot(r2x, r2y)
            plt.plot(r3x, r3y)
        else: #Orientación contraria
            r1x = [point2x, point3x]
            r1y = [point2y, point3y]
            r2x = [point2x, point1x]
            r2y = [point2y, point1y]
            r3x = [point3x, point4x]
            r3y = [point3y, point4y]
            plt.plot(r1x, r1y)
            plt.plot(r2x, r2y)
            plt.plot(r3x, r3y)
    #Si el orden es mayor que 1, calculamos los puntos medios de manera recursiva y también según su orientación
    if order > 1:
        x1 = x + size / 2
        y1 = y - size / 2
        x2 = x + size / 2
        y2 = y + size / 2
        x3 = x - size / 2
        y3 = y + size / 2
        x4 = x - size / 2
        y4 = y - size / 2
        if orientation == 1: #Orientación hacia la derecha
            curvaHilbert(order - 1, x1, y1, size / 2, -2)
            curvaHilbert(order - 1, x2, y2, size / 2, 0)
            curvaHilbert(order - 1, x3, y3, size / 2, 1)
            curvaHilbert(order - 1, x4, y4, size / 2, 1)
            point1x = x - size / 2 ** order
            point1y = y - size / 2 ** order
            point2x = x - size / 2 ** order
            point2y = y + size / 2 ** order
            r1x = [point1x, point2x]
            r1y = [point1y, point2y]
            plt.plot(r1x, r1y)
            point3x = x - size / 2 ** order
            point3y = y - (2 ** order - 1) * size / 2 ** order
            point4x = x + size / 2 ** order
            point4y = y - (2 ** order - 1) * size / 2 ** order
            r2x = [point3x, point4x]
            r2y = [point3y, point4y]
            plt.plot(r2x, r2y)
            point5x = x - size / 2 ** order
            point5y = y + (2 ** order - 1) * size / 2 ** order
            point6x = x + size / 2 ** order
            point6y = y + (2 ** order - 1) * size / 2 ** order
            r3x = [point5x, point6x]
            r3y = [point5y, point6y]
            plt.plot(r3x, r3y)
        elif orientation == -2: #Orientación contraria
            curvaHilbert(order - 1, x1, y1, size / 2, 1)
            curvaHilbert(order - 1, x2, y2, size / 2, -2)
            curvaHilbert(order - 1, x3, y3, size / 2, -2)
            curvaHilbert(order - 1, x4, y4, size / 2, -1)
            point1x = x - size / 2 ** order
            point1y = y + size / 2 ** order
            point2x = x + size / 2 ** order
            point2y = y + size / 2 ** order
            r1x = [point1x, point2x]
            r1y = [point1y, point2y]
            plt.plot(r1x, r1y)
            point3x = x - (2 ** order - 1) * size / 2 ** order
            point3y = y - size / 2 ** order
            point4x = x - (2 ** order - 1) * size / 2 ** order
            point4y = y + size / 2 ** order
            r2x = [point3x, point4x]
            r2y = [point3y, point4y]
            plt.plot(r2x, r2y)
            point5x = x + (2 ** order - 1) * size / 2 ** order
            point5y = y - size / 2 ** order
            point6x = x + (2 ** order - 1) * size / 2 ** order
            point6y = y + size / 2 ** order
            r3x = [point5x, point6x]
            r3y = [point5y, point6y]
            plt.plot(r3x, r3y)
        elif orientation == -1: #Orientación hacia la izquierda
            curvaHilbert(order - 1, x1, y1, size / 2, -1)
            curvaHilbert(order - 1, x2, y2, size / 2, -1)
            curvaHilbert(order - 1, x3, y3, size / 2, 0)
            curvaHilbert(order - 1, x4, y4, size / 2, -2)
            point1x = x + size / 2 ** order
            point1y = y - size / 2 ** order
            point2x = x + size / 2 ** order
            point2y = y + size / 2 ** order
            r1x = [point1x, point2x]
            r1y = [point1y, point2y]
            plt.plot(r1x, r1y)
            point3x = x - size / 2 ** order
            point3y = y + (2 ** order - 1) * size / 2 ** order
            point4x = x + size / 2 ** order
            point4y = y + (2 ** order - 1) * size / 2 ** order
            r2x = [point3x, point4x]
            r2y = [point3y, point4y]
            plt.plot(r2x, r2y)
            point5x = x - size / 2 ** order
            point5y = y - (2 ** order - 1) * size / 2 ** order
            point6x = x + size / 2 ** order
            point6y = y - (2 ** order - 1) * size / 2 ** order
            r3x = [point5x, point6x]
            r3y = [point5y, point6y]
            plt.plot(r3x, r3y)
        else: #Orientación normal
            curvaHilbert(order - 1, x1, y1, size / 2, 0)
            curvaHilbert(order - 1, x2, y2, size / 2, 1)
            curvaHilbert(order - 1, x3, y3, size / 2, -1)
            curvaHilbert(order - 1, x4, y4, size / 2, 0)
            point1x = x - size / 2 ** order
            point1y = y - size / 2 ** order
            point2x = x + size / 2 ** order
            point2y = y - size / 2 ** order
            r1x = [point1x, point2x]
            r1y = [point1y, point2y]
            plt.plot(r1x, r1y)
            point3x = x - (2 ** order - 1) * size / 2 ** order
            point3y = y - size / 2 ** order
            point4x = x - (2 ** order - 1) * size / 2 ** order
            point4y = y + size / 2 ** order
            r2x = [point3x, point4x]
            r2y = [point3y, point4y]
            plt.plot(r2x, r2y)
            point5x = x + (2 ** order - 1) * size / 2 ** order
            point5y = y - size / 2 ** order
            point6x = x + (2 ** order - 1) * size / 2 ** order
            point6y = y + size / 2 ** order
            r3x = [point5x, point6x]
            r3y = [point5y, point6y]
            plt.plot(r3x, r3y)

def casoDePrueba():
    try:
        print("Introduzca el orden de la curva de Hilbert")
        orden = int(input())
        curvaHilbert(orden,1,1,1,0)
        plt.show()
        return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass

