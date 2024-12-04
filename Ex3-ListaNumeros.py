#Escribe un programa que pida dous números enteiros e escriba a lista de números consecutivos entre eles, en orde crecente ou decrecente
x = int (input ("Introduce un numero: "))
y = int (input ("Introduce otro numero: "))

numberIn =  [x,y]


if numberIn [1] > numberIn [0]:
    for i in range (numberIn[0], numberIn[1]+1):
        print (i)

else:
    for i in range (numberIn[1],numberIn[0]):
        print (i)