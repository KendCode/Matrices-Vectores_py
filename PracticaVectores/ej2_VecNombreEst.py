nombres_estudiantes = []

# Solicitar 
print("Introduce los nombres de 5 estudiantes:")
for i in range(5):
    nombre = input(f"Estudiante {i+1}: ")
    nombres_estudiantes.append(nombre)

# orden inverso
nombres_inverso = nombres_estudiantes[::-1]

# Mostrar el vector 
print("Los nombres de los estudiantes en orden inverso son:")
for nombre in nombres_inverso:
    print(nombre, end=' ')