def calcular_transpuesta(matriz):
    filas_originales = len(matriz)
    columnas_originales = len(matriz[0])
    transpuesta = []
    for j in range(columnas_originales):
        fila_transpuesta = []
        for i in range(filas_originales):
            fila_transpuesta.append(matriz[i][j])
        transpuesta.append(fila_transpuesta)
    return transpuesta

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
def main():
    # Definir la matriz original
    matriz_original = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz_transpuesta = calcular_transpuesta(matriz_original)
    print("La transpuesta de la matriz es:")
    mostrar_matriz(matriz_transpuesta)

if __name__ == "__main__":
    main()

