import functools
# 1
def obtener_impares(lista):
  impares = filter(lambda x: x % 2 != 0, lista)
  return list(impares)
# 2
def sumar_elementos(lista):
  suma = functools.reduce(lambda x, y: x + y, lista)
  return suma
# 3 Ejemplo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4
impares = obtener_impares(lista)
# 5
suma = sumar_elementos(impares)
# 6
print(f"La suma de los elementos impares de {lista} es {suma}")
