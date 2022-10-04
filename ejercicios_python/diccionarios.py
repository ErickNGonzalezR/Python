def main ():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    for llave in mi_diccionario.keys():
        print(llave)
        return llave


    for llave in mi_diccionario.values():
        print(llave)
        return llave



    for llave, contenido in mi_diccionario.items():
        print(llave + contenido)       
        return llave

if __name__=='__main__':
    main()    