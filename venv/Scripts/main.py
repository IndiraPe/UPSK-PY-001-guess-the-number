import random


""" Obtener el número random """
def numRandom():
    return random.randint(1, 100)


""" Obtener el nombre del jugador """
def namePlayer():
    return input('\nHola!!, ingresa tu nombre: ')


""" Bienvenida al jugador """
def welcomeTheGame():
    print('Bienvenido(a) ' + namePlayer() + ', intenta ganarle a la computadora adivinando el número primero entre 1 - 100. Comencemos!!!\nYa tengo el número, Tu empiezas!!!\n')
    initGame()


""" Obtener el número ingresado del jugador """
def obtainNumOfPlayer():       
    return input('\nAdivina el número: ')


""" Que empiece el juego """
def initGame():

    arrNumOfPlayer = []
    arrNumOfComputer = []
    obtainNumRandom = numRandom()

    while True:
        try: 
            numOfPlayer = obtainNumOfPlayer()
            arrNumOfPlayer.append(int(numOfPlayer))
            computerPlayer = random.randint(1, 100)
            arrNumOfComputer.append(computerPlayer)

            if int(numOfPlayer) == obtainNumRandom:
                print('------------------------------------------------------------------------')
                print('Felicidades!!! Venciste a la computadora\n')
                break
            elif int(numOfPlayer) < 0 or int(numOfPlayer) > 100:
                print('Recuerda que solo pueden ser números entre 1 - 100!!')
            elif int(numOfPlayer) > obtainNumRandom:
                print('Es muy alto!!')                
            else:
                print('Es muy bajo!!')

            print('------------------------------------------------------------------------')
            print('Computadora: Es mi turno!! Creo que el número es: ' + str(computerPlayer))

            if computerPlayer == obtainNumRandom:
                print('------------------------------------------------------------------------')
                print('La computadora ganó, más suerte para la próxima!!\n')
                break
            elif computerPlayer > obtainNumRandom:
                print('Es muy alto!!')
                print('------------------------------------------------------------------------\n')
            else:
                print('Es muy bajo!!')
                print('------------------------------------------------------------------------\n')
        
        except:
            print('Debes ingresar solo números!!')
            
    print('Tus intentos fueron: ', arrNumOfPlayer, '\n')
    print('Los intentos de la computadora fueron: ', arrNumOfComputer, '\n')
    return True



if __name__ == "__main__":
    welcomeTheGame()