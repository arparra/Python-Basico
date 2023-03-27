class Persona:
    def __init__(self):
        self.tipoDoc = ""
        self.documento = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirDatos(self):
        self.tipoDoc = input("Ingrese Tipo de documento: ")
        self.documento = input("Ingrese Número de documento: ")
        self.nombre = input("Ingrese Nombre de la persona: ")
        self.apellido = input("Ingrese Apellido de la persona: ")
        self.peso = float(input("Ingrese Peso de la persona en kg: "))
        self.estatura = float(input("Ingrese Estatura de la persona en mts: "))
        self.edad = int(input("Ingrese la edad de la persona: "))
        self.sexo = input("Escoja el Sexo de la persona (M/F): ").upper()

    def mostrarPersona(self):
        print("Tipo de documento:", self.tipoDoc, "\n"
              "Número de documento:", self.documento, "\n"
              "Nombre:", self.nombre, "\n"
              "Apellido:", self.apellido, "\n"
              "Peso:", self.peso, "\n"
              "Estatura:", self.estatura, "\n"
              "Edad:", self.edad, "\n"
              "Sexo:", self.sexo, "\n")
        
    def calcularImc(self):
        pesoActual = self.peso / (self.estatura ** 2)
        if pesoActual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayorEdad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")