from googlesearch import search

print("""Bienvenido a Wikipedia de Phabiot \nPuedo ofrecerle lo siguiente: 
      1. Busqueda normal
      """)


Busqueda=input("Antes de realizar la busqueda debo advertirle de que solo se mostraran enlaces y nada visual.\n¿Que desea buscar? ")
results=search(Busqueda, lang="es", tld="com")
lang="es"
tld="com"
for r in results:
    print(r)