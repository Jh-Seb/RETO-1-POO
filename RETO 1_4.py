# Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
def leer():
    S = input("Digite los números separados por comas: ").split(',')
    S = [int(x) for x in S]
    return S

def SumaMayor(M):
    if len(M) < 2:
        return None  # No hay suficientes elementos para calcular la suma

    mayor_suma = M[0] + M[1]
    for i in range(1, len(M) - 1):
        suma = M[i] + M[i + 1]
        if suma > mayor_suma:
            mayor_suma = suma
    return mayor_suma

# PROGRAMA PRINCIPAL
M = leer()
resultado = SumaMayor(M)
if resultado is not None:
    print("La mayor suma entre dos elementos consecutivos es:", resultado)
else:
    print("La lista debe contener al menos dos elementos.")
