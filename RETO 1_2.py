def esPalindrome(a):
    for i in range(len(a)):
        if a[i] != a[-i-1]:
            return False
        return True

# PROGRAMA PRINCIPAL
a = str(input("DIGITE LA CADENA: "))
d = esPalindrome(a)
print("La cadena es palíndromo:", d)
