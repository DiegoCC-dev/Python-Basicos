import hashlib

def calcular_sha1(ficheiro):
    sha1 = hashlib.sha1()
    with open(ficheiro, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

# Proba de exemplo
ficheiro = input("Introduce a ruta do ficheiro: ")
print(f"O SHA1 do ficheiro é: {calcular_sha1(ficheiro)}")
