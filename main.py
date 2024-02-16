import random

numRandom = random.randint(1, 100)

namePlayer = input('Hola!!, ingresa tu nombre: ')
print('Bienvenido(a) ' + namePlayer + ', intenta ganarle a la computadora adivinando el número primero. Comencemos!!!\nYa tengo el número, Tu empiezas!!!')
numOfPlayer = input('Adivina el número: ')

if int(numOfPlayer) == numRandom:
    print('Felicidades!!! Venciste a la computadora')
elif int(numOfPlayer) > numRandom:
    print('Es muy alto!!')
else:
    print('Es muy bajo!!')