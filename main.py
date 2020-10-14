import random


def saludoInicial(name, age):
    print(f'Hola {name}')
    print(f'Tienes {age} años')
    if age >= 30:
        print('Ya estas un poco grande para jugar\n*<< Mejor ponte a trabajar jajaja >>*')
    elif age >= 20:
        print('Es la edad ideal para jugar')
        print('EMPECEMOS EL JUEGO')


def escogeLongitud(longDif):
    print('Selecciona una longitud, mientras mas grande mas dificultad.')
    longDif = input('''   
        1.- 1 al 10
        2.- 1 al 20
        3.- 1 al 30
    ''')
    return longDif


if __name__ == "__main__":
    print(' B I E N V E N I D O')
    print('Este es el Juego Numero Secreto')
    print('Tienes que dar un numero, te dare pistas y debes adivinar el numero en 3 intentos')

    player = input('Escribe tu Nickname: ')
    age = int(input('Escribe tu Edad: '))
    saludoInicial(player, age)
    longDif = escogeLongitud(age)

    print(f'La dificultad es: {longDif}')
