# 1
paises = input("Introduce una lista de países (separados por comas): ")
# 2
lista_paises = paises.split(",")
# 3
conjunto_paises = set(lista_paises)
# 4
lista_ordenada = sorted(conjunto_paises)
print(", ".join(lista_ordenada))
