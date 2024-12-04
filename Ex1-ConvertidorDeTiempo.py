#Programa para pasar una cantidad de segundos a minutos y segundos

#Input del usuario
tiempoIn = int(input("Introduce la cantidad de segundos: ")) 



minutos = int (tiempoIn/60)
segundos = int (tiempoIn%60)

print ( f"{tiempoIn} segundos son:  {minutos}  minutos y   {segundos}  segundos")