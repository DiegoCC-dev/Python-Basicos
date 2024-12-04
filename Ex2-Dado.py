#Tira 2 dados y compara el resultado
import random


def D6():
    return random.randint(1,6)
    
def compare():
    dado1=D6()
    dado2=D6()

    print (f"Dado 1: {dado1}, Dado 2: {dado2}")

    if int(dado1) > int(dado2):
        print("Dado 1 es mayor que Dado 2")


    elif int(dado1) < int(dado2):
        print("Dado 2 es mayor que Dado 1")
    

    else:
        print("Empate")
    

    

compare();


    


