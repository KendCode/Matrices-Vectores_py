def calcular_determinante(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        print("Error: La matriz debe ser cuadrada de 3x3 para calcular la determinante.")
        return None
    det = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + \
          (matriz[0][1] * matriz[1][2] * matriz[2][0]) + \
          (matriz[0][2] * matriz[1][0] * matriz[2][1]) - \
          (matriz[0][2] * matriz[1][1] * matriz[2][0]) - \
          (matriz[0][0] * matriz[1][2] * matriz[2][1]) - \
          (matriz[0][1] * matriz[1][0] * matriz[2][2])
    return det
def main():
    matriz = [
        [2, -3, 1],
        [5, 4, 7],
        [0, -1, 3]
    ]
    determinante = calcular_determinante(matriz)
    if determinante is not None:
        print("La determinante de la matriz es:", determinante)

if __name__ == "__main__":
    main()


