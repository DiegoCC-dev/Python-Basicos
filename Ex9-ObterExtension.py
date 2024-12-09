import os

ruta = input("Introduce a ruta do ficheiro: ")
extensao = os.path.splitext(ruta)[1]
print(f"A extensión do ficheiro é: {extensao}")
