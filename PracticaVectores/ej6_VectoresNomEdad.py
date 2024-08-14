def main():
    
    cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))

   
    nombres = []
    edades = []

    for i in range(cantidad_alumnos):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        
        nombres.append(nombre)
        edades.append(edad)

    print("\nAlumnos mayores de edad:")
    for nombre, edad in zip(nombres, edades):
        if edad >= 18:
            print(f"{nombre}: {edad} años")

    max_edades = sorted(edades, reverse=True)[:2]
    print("\nLos dos alumnos mayores:")
    for nombre, edad in zip(nombres, edades):
        if edad in max_edades:
            print(f"{nombre}: {edad} años")

if __name__ == "__main__":
    main()
