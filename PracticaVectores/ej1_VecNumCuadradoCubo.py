#RANDOM LIBRERIAS
import random

#funcion principal
def run():
    vectorNumeros=[]
    ne = 10

    for i in range(ne):
        vectorNumeros.append(random.randint(1,10))

    print(vectorNumeros)

    #obtenemos el cuadrado de cada valor
    for elementos in vectorNumeros:
        print(elementos**2, end=' ')
    print()
    #obtenemos el cubo de cada valor
    for elementos in vectorNumeros:
        print(elementos**3, end=' ')

if __name__=='__main__':
    run()