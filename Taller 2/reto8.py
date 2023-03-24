num_notas = int(input("Por favor ingrese la cantidad de notas a evaluar: "))

notas = []
for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    while nota < 0.0 or nota > 5.0:
        nota = float(input(f"Ingrese una nota válida (entre 0.0 y 5.0) para la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / num_notas

if promedio < 3.0:
    print("\nLa nota fue menor de 3, Reprobo")
    nota_final = 0.0
elif promedio >= 3.0 and promedio < 4.0:
    print("\nLa nota esta entre 3 y 4, Paso raspando")
    nota_final = 3.5
else:
    print("\nLa nota es mayor de 4, Aprobo con buenos resultados")
    nota_final = 5.0

print(f"\nLa nota final es: {nota_final}")