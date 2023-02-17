c1 = str(input("Ingresa la primera palabra: "))
c2 = str(input("Ingresa la segunda palabra: "))
c1 = c1.replace(" ","")
c2 = c2.replace(" ","")
c2 = set(c2)
c1 = set(c1)
n1 = len(c1)
n2 = len(c2)
if n1 == n2 and c1==c2:
    print("Las palabras ingresadas son anagramas")
else:
    print("Las palabras ingresadas no son anagramas")



