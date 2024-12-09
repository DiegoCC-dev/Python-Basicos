alfabeto_nato = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whisky', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'
}

def imprimir_nato(palabra):
    for letra in palabra.upper():
        if letra.isalpha():
            print(f"{letra}: {alfabeto_nato[letra]}")

# Proba de exemplo
palabra = input("Introduce unha palabra: ")
imprimir_nato(palabra)
