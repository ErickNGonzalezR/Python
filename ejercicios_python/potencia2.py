def main():
    numero = input("Escribe un numero: ")
    acumulador = 0
    numero = int(numero)
    while numero >= acumulador:
        potencia = 2**acumulador   
        acumulador = acumulador + 1
    

    print(potencia)
        

if __name__=='__main__':
    main()
