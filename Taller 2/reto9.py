num_competidores = int(input("Ingrese la cantidad de competidores: "))

competidores = {}

for i in range(num_competidores):
    nombre = input("Ingrese el nombre del competidor {}: ".format(i+1))
    competidores[nombre] = None

for nombre in competidores:
    tiempo = float(input("Ingrese el tiempo de {}: ".format(nombre)))
    competidores[nombre] = tiempo

print("\nTiempos registrados:")
for nombre, tiempo in competidores.items():
    print("{}: {}".format(nombre, tiempo))

ganador = min(competidores, key=competidores.get)
print("\nEl ganador es: {} con un tiempo de {} segundos".format(ganador, competidores[ganador]))