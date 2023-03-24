instructores2503816 = {}

while True:
    print("\n=== MENU ===")
    print("1. Agregar/modificar instructor")
    print("2. Buscar instructor")
    print("3. Borrar instructor")
    print("4. Listar instructores")
    print("5. Salir")
    opcion = input("Ingrese una opción (1-5): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del instructor: ")
        if nombre in instructores2503816:
            print(f"El instructor {nombre} ya está registrado.")
            print(f"Materia: {instructores2503816[nombre]['materia']}")
            telefono = input("Ingrese el nuevo número de teléfono (o enter para dejarlo sin cambios): ")
            if telefono != "":
                instructores2503816[nombre]['telefono'] = telefono
        else:
            materia = input("Ingrese la materia que dicta: ")
            telefono = input("Ingrese el número de teléfono: ")
            instructores2503816[nombre] = {'materia': materia, 'telefono': telefono}
            print(f"El instructor {nombre} ha sido registrado.")

    elif opcion == "2":
        busqueda = input("Ingrese un texto de búsqueda: ")
        resultados = []
        for nombre, datos in instructores2503816.items():
            if nombre.startswith(busqueda):
                resultados.append(nombre)
        print("Resultados de la búsqueda:")
        for nombre in resultados:
            print(f"Nombre: {nombre} - Materia: {instructores2503816[nombre]['materia']} - Teléfono: {instructores2503816[nombre]['telefono']}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del instructor a borrar: ")
        if nombre in instructores2503816:
            confirmacion = input(f"¿Está seguro que desea borrar al instructor {nombre}? (s/n): ")
            if confirmacion.lower() == "s":
                del instructores2503816[nombre]
                print(f"El instructor {nombre} ha sido borrado.")
        else:
            print(f"No se encontró al instructor {nombre} en la agenda.")

    elif opcion == "4":
        print("\nInstructores registrados:")
        for nombre, datos in instructores2503816.items():
            print(f"Nombre: {nombre} - Materia: {datos['materia']} - Teléfono: {datos['telefono']}")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")