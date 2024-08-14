def multiplicar_matrices(matriz1, matriz2):
    
    if len(matriz1[0]) != len(matriz2):
        print("Error: Las matrices no tienen dimensiones compatibles para la multiplicación.")
        return None
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
           
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matriz2 = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    resultado = multiplicar_matrices(matriz1, matriz2)
    if resultado:
        print("El resultado de la multiplicación de las dos matrices es:")
        mostrar_matriz(resultado)
if __name__ == "__main__":
    main()
