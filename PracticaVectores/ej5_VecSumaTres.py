def sumar_vectores(vector1, vector2):
    vector3 = []
    5
    for i in range(len(vector1)):
        suma = vector1[i] + vector2[i]
        vector3.append(suma)
    
    return vector3

def main():
    vector1 = []
    vector2 = []
    vector3 = []
    print("Ingrese los valores para el vector1:")
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        vector1.append(valor)

    print("\nIngrese los valores para el vector2:")
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        vector2.append(valor)

    vector3 = sumar_vectores(vector1, vector2)

    print("\nLa suma de los elementos de vector1 y vector2 es:")
    print(vector3)

if __name__ == "__main__":
    main()
