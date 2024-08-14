import random

def ordena(v):
    ne = len(v)

    for i in range(ne - 1):
        for j in range(i + 1, ne):  
            if v[i] > v[j]:  
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    print("Vector ordenado de menor a mayor:", v)

def run():
    vector = []
    ne = int(input('Inserte el numero de elementos del vector: '))
    for i in range(ne):
        vector.append(random.randint(1, 20))
    print("Vector original:", vector)
    ordena(vector)

if __name__ == '__main__':
    run()

