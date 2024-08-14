def main():
    #número de filas y columnas
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    #  matriz vacía
    matriz = []

    # Llenar la matriz 
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento de la posición [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    # Mostrar la matriz
    print("La matriz ingresada es:")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()
