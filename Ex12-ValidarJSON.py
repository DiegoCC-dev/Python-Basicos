import json

def comprobar_json(ficheiro):
    try:
        with open(ficheiro, 'r') as f:
            json.load(f)
        print("O ficheiro JSON é válido.")
    except (json.JSONDecodeError, FileNotFoundError):
        print("O ficheiro JSON non é válido.")

# Proba de exemplo
ficheiro = input("Introduce a ruta do ficheiro JSON: ")
comprobar_json(ficheiro)
