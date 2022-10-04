menu = """
Bienvenido a el conversor de moneda

1. Pesos Colombianos 
2. Pesos Argentinos
3. Pesos Mexicanos
"""
opcion = input(menu)
opcion = int(opcion)
def conversor_moneda (valor_nomeda,pesos):
    dolares =  pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares) 
    print("Tienes $" + dolares +" dolares")
if opcion ==1 :
    conversor_moneda(3800,float("Cuantos pesos Colombianos tienes"))
    

elif opcion ==2:
    pesos = float(input ("Cuantos pesos Argentinos tienes"))
    valor_dolar = 60
    conversor_moneda()

elif opcion ==3:
    pesos = float(input ("Cuantos pesos Mexicanos tienes"))
    valor_dolar = 24
    conversor_moneda()

else:
    print("porfavor elige una opcion correcta")    
