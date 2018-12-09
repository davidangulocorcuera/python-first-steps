import random

acierto = (0)
randomNum = random.randrange(1,100)

while acierto == (0):

    num = input()
    if num == randomNum:
        print("Acertaste!")
        acierto = (1)

    elif num > randomNum:
        print("El numero introducido es mayor")

    elif num < randomNum:
        print("El numero introducido es menor")