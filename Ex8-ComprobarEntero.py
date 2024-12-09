def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

# Proba de exemplo
cadena = input("Introduce unha cadea: ")
if es_entero(cadena):
    print("Pódese convertir a un número enteiro.")
else:
    print("Non se pode converter a un número enteiro.")
