def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Error: Las matrices deben tener las mismas dimensiones para poder sumarlas.")
        return None
    suma = []
    for i in range(len(matriz1)):  
        fila_suma = []  
        for j in range(len(matriz1[0])):  
            suma_elemento = matriz1[i][j] + matriz2[i][j]  
            fila_suma.append(suma_elemento)  
        suma.append(fila_suma)  
    return suma  
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)  

def main():
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    # Sumar las matrices
    matriz_suma = suma_matrices(matriz1, matriz2)

    # Mostrar la matriz resultante
    if matriz_suma:  
        print("La suma de las dos matrices es:")
        mostrar_matriz(matriz_suma)  

if __name__ == "__main__":
    main()
