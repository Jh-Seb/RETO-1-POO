# OPERACIONES BASICAS
def leeroperacion():
    s = input('Ingresar la operacion en formato (n1,n2,"+"): ')
    s = s[1:-1]
    e = s.split(',')
    for i in range(2):
        e[i] = int(e[i])
    e[2] = e[2].strip().strip('"').strip("'")  # Asegurarse de que el operador sea un string limpio
    return e

def ejecutaroperacion(M):
    if M[2] == '+':
        resultado = M[0] + M[1]
    elif M[2] == '-':
        resultado = M[0] - M[1]
    elif M[2] == '*':
        resultado = M[0] * M[1]
    elif M[2] == '/':
        resultado = M[0] / M[1]
    return resultado

# PROGRAMA PRINCIPAL
M = leeroperacion()
resultado = ejecutaroperacion(M)
print(resultado)