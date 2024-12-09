import re

cadena = 'lorem 12 abc 89. como son 34 e 211? xa non sae 512'
numeros = re.findall(r'\d+', cadena)
print(numeros)
