# Python-Basico
Python trimestre IV
import random
ppt = random.randint(1,3)

contin = "s" or "S"

while contin == "s" or contin=="S":
    
    print("Bienvenido... Vamos a jugar piedra, papel o tijera!!! \n"
          "Seleccione: \n"
          "1 para Piedra\n"
          "2 para Papel\n"
          "3 para Tijera\n"
          "Por favor marque el numero ahora: ")
    
    num = int(input())
    print("Usted escogio: ",num)
                    
    if num >= 4:
        print("Por favor marque una opcion valida\n"
              "1 Piedra\n"
              "2 Papel\n"
              "3 Tijera")
        
    elif ppt == 1 and num == 1:
        print (ppt," Piedra\n"
               "Es un empate!\n"
               "Los dos sacaron Piedra")
        
    elif ppt ==1 and num == 2:
        print (ppt," Piedra\n"
               "Perfecto, Ganaste!\n"
               "Escogiste Papel")
               
    elif ppt ==1 and num == 3:
        print (ppt,"Piedra\n"
               "Que triste Perdiste\n"
               "Escogiste Tijera")
        
    elif ppt == 2 and num == 2:
        print(ppt," Papel\n"
               "Es un empate!\n"
               "Los dos sacaron Papel")
        
    elif ppt == 2 and num == 1:
        print(ppt,"Papel\n"
               "Que triste Perdiste\n"
               "Escogiste Piedra")
        
    elif ppt == 2 and num == 3:
        print(ppt," Papel\n"
               "Perfecto, Ganaste!\n"
               "Escogiste Tijera")
        
    elif ppt == 3 and num == 3:
        print(ppt," Tijera\n"
               "Es un empate!\n"
               "Los dos sacaron Tijera")
        
    elif ppt == 3 and num == 1:
        print(ppt," Tijera\n"
              "Perfecto, Ganaste!\n"
               "Escogiste Piedra")
    else:
        print(ppt," Tijera\n"
              "Que triste Perdiste\n"
              "Escogiste Papel")
    
    contin = input("Quieres volver a jugar presiona s/S\n"
                   "si no desesas continuar presiona cualquier tecla para finalizar\n")
