from collections import Counter

cadena = input("Introduce unha cadea: ")
vocais = 'aeiouAEIOU'
contador = Counter([letra for letra in cadena if letra in vocais])

for vocal, cantidade in contador.items():
    print(f"A letra {vocal} aparece {cantidade} veces.")
