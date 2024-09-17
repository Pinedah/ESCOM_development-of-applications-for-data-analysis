#! python3
# Tarea 1

import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)


"""
Desarrolla un programa que determine si es posible construir una cantidad exacta de dinero utilizando un número específico de monedas. Por ejemplo:

Es posible obtener un total de $1.00 usando cuatro monedas si todas son de 25 centavos.
Sin embargo, no es posible obtener un total de $1.00 con cinco monedas.
Por otro lado, es posible formar $1.00 con seis monedas si se utilizan tres de 25 centavos, dos de 10 centavos, y una de 5 centavos.
Del mismo modo, un total de $1.25 puede formarse usando cinco u ocho monedas, pero no se puede lograr usando cuatro, seis, o siete monedas.
Su programa debe recibir como entrada el importe en dólares y el número de monedas que el usuario desea utilizar. Luego, debe mostrar un mensaje claro indicando si es posible formar la cantidad especificada con el número de monedas indicado. Para este problema, asume que tienes monedas de 25, 10, 5 y 1 centavos. La solución debe implementarse utilizando recursividad y no debe incluir ningún tipo de ciclo.
"""

def puede_formar_monto(monedas, num_monedas, monto):
    
    print("Recursividadddddddddd\n")
    print(f"num monedas: {num_monedas}")
    print(f"monto: {monto}")

    if monto == 0 and num_monedas == 0:
        return True
    
    if num_monedas == 0 or monto < 0:
        return False
    
    # Para cada tipo de moneda, intenta restar su valor y llama recursivamente
    if puede_formar_monto(monedas, num_monedas - 1, monto - monedas[0]): # 25
        return True
    if puede_formar_monto(monedas, num_monedas - 1, monto - monedas[1]): # 10
        return True
    if puede_formar_monto(monedas, num_monedas - 1, monto - monedas[2]): # 5
        return True
    if puede_formar_monto(monedas, num_monedas - 1, monto - monedas[3]): # 1
        return True
    
    return False


def estandarizar_valores(valor):
    return valor * 100

def main():
    while True:
        try:
            importe = float(input("Ingrese el importe (en dls): $"))
            num_monedas = int(input("Ingrese la cantidad de monedas: "))
            break
        except ValueError:
            print("!!! Por favor ingrese un valor válido.\n")

    puede = False 
    # monedas = PosibleCambio(a,importe, num_monedas)
    monedas = [25, 10, 5, 1]
    importe = estandarizar_valores(importe)

    puede = puede_formar_monto(monedas, num_monedas, importe)

    if puede:
        print(f"Es posible formar ¢{importe/100} con {num_monedas} monedas")
    else:
        print(f"NO es posible formar ¢{importe/100} con {num_monedas} monedas")

if __name__ == '__main__':
    main()