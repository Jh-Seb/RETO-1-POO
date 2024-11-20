#Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
def leer():
    S = input("Digite las palabras separadas por comas: ").split(',')
    return S
#def contar(s):
#   D = {}
#    for i in s:
#        for x in i:
#            if x not in D:
#                D[x] = 1
#           else:
#               D[x] += 1
#    return D
def filtrar_elementos_con_mismos_caracteres(l):
    r = []
    for p in l:
        if any(sorted(p) == sorted(otra) for otra in l if p != otra):
            r.append(p)
    return r

#PROGRAMA PRINCIPAL
M = leer()
#C = contar(M)
r = filtrar_elementos_con_mismos_caracteres(M)
if len(r) == 0:
    print("No hay palabras con los mismos caracteres")
else:
    print(r)