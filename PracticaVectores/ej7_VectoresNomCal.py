def main():
    cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))
    nombres = []
    notas_finales = []
    for i in range(cantidad_alumnos):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        nota_final = float(input(f"Ingrese la nota final de {nombre}: "))
        nombres.append(nombre)
        notas_finales.append(nota_final)
    print("\nAlumnos Aprobados:")
    for nombre, nota_final in zip(nombres, notas_finales):
        if nota_final >= 61:
            print(f"{nombre}: {nota_final} puntos")

    print("\nAlumnos Reprobados sin opción a 2do turno:")
    for nombre, nota_final in zip(nombres, notas_finales):
        if nota_final < 40:
            print(f"{nombre}: {nota_final} puntos")
if __name__ == "__main__":
    main()
