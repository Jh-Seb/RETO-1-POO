def esPalindrome(a):
    c = ''
    for i in range(len(a) - 1, -1, -1):
        c += a[i]


    return c == a

# PROGRAMA PRINCIPAL
a = str(input("DIGITE LA CADENA: "))
d = esPalindrome(a)
print("La cadena es palíndromo:", d)
