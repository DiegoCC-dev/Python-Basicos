import requests

def obter_ratio_conversion(moeda_orixe, moeda_destino):
    url = f"http://freecurrencyrates.com/api/action.php?do=cvals&iso={moeda_orixe}&f={moeda_destino}&v=1&s=cbr"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        datos = resposta.json()
        return datos['rate']
    else:
        return None

# Proba de exemplo
moeda_orixe = input("Introduce a moeda de orixe (exemplo: USD): ")
moeda_destino = input("Introduce a moeda de destino (exemplo: EUR): ")
ratio = obter_ratio_conversion(moeda_orixe, moeda_destino)
if ratio:
    print(f"A ratio de conversión de {moeda_orixe} a {moeda_destino} é: {ratio}")
else:
    print("Non se puido obter a ratio de conversión.")
