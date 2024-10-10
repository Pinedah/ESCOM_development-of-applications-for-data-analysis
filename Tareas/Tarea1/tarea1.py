#! python3

# TODO: el problema no lo dice, pero podriamos encontrar la lista de que monedas ocupar cuando sea el caso

def PosibleCambio(monedas, importe, num_monedas, index = 0, memo = None):
    if memo is None:
        memo = {}
    if importe == 0 and num_monedas == 0:
        return True
    if importe < 0 or num_monedas < 0 or index >= len(monedas):
        return False
    if (importe, num_monedas, index) in memo:
        return memo[(importe, num_monedas, index)]
    usar_moneda = PosibleCambio(monedas, importe - monedas[index], num_monedas - 1, index, memo)

    no_usar_moneda = PosibleCambio(monedas, importe, num_monedas, index + 1, memo)

    memo[(importe, num_monedas, index)] = usar_moneda or no_usar_moneda
    return memo[(importe, num_monedas, index)]

def main():
  tiposDeMonedas = [1,5,10,25]
  while True:
      try:
          importe = int(input("Ingrese el importe (en centavos): ¢"))
          num_monedas = int(input("Ingrese la cantidad de monedas: "))
          break
      except ValueError:
          print("!!! Por favor ingrese un valor válido.\n")

  monedas = PosibleCambio(tiposDeMonedas, importe, num_monedas)
  if monedas:
    print(f"Es posible formar ¢{importe} con {num_monedas} monedas")
  else:
    print(f"NO es posible formar ¢{importe} con {num_monedas} monedas")

if __name__ == '__main__':
    main()
    