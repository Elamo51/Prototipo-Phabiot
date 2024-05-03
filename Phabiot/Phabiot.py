#Importaciones
import Calculadora_de_phabiot, Wikipedia_de_phabiot


#Menú en pantalla
print("Hola, bienvenido al 'Alpha' de 'Phabiot', el robot ayudante, solo tiene funciones primordiales y por ello pido comprension. \nLuego de esta introduccion ya puede acceder al Robot")
print("------------------------------------------------------------")
print("¿Qué desea? Puedo ofrecerlo varias opciones:")
print("""
      1. Calculadora            4. Temporizador
      2. Wikipedia              5. Creador de comandos de Aldeanos
      3. Clima
      """)

#Elecciones
Eligio = input("Seleccione algo: ")

#Importaciones
import Calculadora_de_phabiot

#Consecuencias de las elecciones
if Eligio==1:
    print(Calculadora_de_phabiot)

elif Eligio==2:
    print(Wikipedia_de_phabiot)