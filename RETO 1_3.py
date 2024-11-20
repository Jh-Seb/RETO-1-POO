def ordenar_lista(x):
    x = x.split(",")
    x = [int(i) for i in x]
    x.sort()
    return x

def esPrimo(x):
    L = []
    for i in x:
        s = True
        if i < 2:
            s = False
        for k in range(2, int(i**0.5) + 1):
            if i % k == 0:
                s = False
                break
        if s:
            L.append(i)
    return L

# PROGRAMA PRINCIPAL
x = input("DIGITE LA LISTA DE NUMEROS SEPARADOS POR COMAS: ")
c = ordenar_lista(x)
d = esPrimo(c)
print("Los numeros primos son:", d)