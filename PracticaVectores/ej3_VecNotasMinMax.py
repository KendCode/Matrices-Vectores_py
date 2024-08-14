def procesar_notas():
    notas = []

    for i in range(1, 6):
        while True:
            nota = float(input(f"Ingresa la nota {i} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10. Intenta de nuevo.")

    nota_media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    print("\nNotas ingresadas:", notas)
    print(f"Nota media: {nota_media:.1f}")
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")

if __name__ == "__main__":
    procesar_notas()
