Calculadora = print("""Bienvenido a la calculadora de Phabiot, ¿que se le ofrece? \nAqui tiene alguna de las opciones que puedo ofrecer ahora mismo:
      1. Suma                  3. Multiplicacion
      2. Resta                 4. Divivision
      """)
Eleccion = int(input("Elija: "))

if Eleccion==1:
    x = int(input("Numero 1 que quieres sumar: "))
    y = int(input("Numero 2 que quieres sumar: "))
    suma=(x+y)
    print(f"El resultado es {suma}")

if Eleccion==2:
    x = int(input("Numero 1 que quieres sumar: "))
    y = int(input("Numero 2 que quieres sumar: "))
    suma=(x-y)
    print(f"El resultado es {suma}")

if Eleccion==3:
    x = int(input("Numero 1 que quieres sumar: "))
    y = int(input("Numero 2 que quieres sumar: "))
    suma=(x*y)
    print(f"El resultado es {suma}")

if Eleccion==4:
    x = int(input("Numero 1 que quieres sumar: "))
    y = int(input("Numero 2 que quieres sumar: "))
    suma=(x/y)
    print(f"El resultado es {suma}")