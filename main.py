import random


""" Obtener el número random """
def numRandom():
    return random.randint(1, 100)


""" Obtener el nombre del jugador """
def namePlayer():
    return input('Hola!!, ingresa tu nombre: ')


""" Bienvenida al jugador """
def welcomeTheGame():
    return print('Bienvenido(a) ' + namePlayer() + ', intenta ganarle a la computadora adivinando el número primero entre 1 - 100. Comencemos!!!\nYa tengo el número, Tu empiezas!!!')


""" Obtener el número ingresado del jugador """
def obtainNumOfPlayer():       
    return input('Adivina el número: ')


""" Que empiece el juego """
def initGame():

    welcomeTheGame()
    arrNumOfPlayer = []
    obtainNumRandom = numRandom()

    while True:
        try: 
            numOfPlayer = obtainNumOfPlayer()
            arrNumOfPlayer.append(int(numOfPlayer))

            if int(numOfPlayer) == obtainNumRandom:
                print('Felicidades!!! Venciste a la computadora')
                break
            elif int(numOfPlayer) < 0 or int(numOfPlayer) > 100:
                print('Recuerda que solo pueden ser números entre 1 - 100!!')
            elif int(numOfPlayer) > obtainNumRandom:
                print('Es muy alto!!')
            else:
                print('Es muy bajo!!')
        
        except:
            print('Debes ingresar solo números!!')
            
    print(arrNumOfPlayer)

initGame()