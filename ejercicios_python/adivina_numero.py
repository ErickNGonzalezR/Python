import random

def main ():
    numero_aleatorio = random.randint(1,100)
    numero = 200
    while numero != numero_aleatorio:
        numero = int(input('Digite un numero: '))
        if numero < numero_aleatorio:
            print('el numero es mayor ')
        else:
            print('El numero es menor ')
    print('haz ganado')


if __name__=='__main__':
    main()