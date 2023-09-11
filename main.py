from forex_python.converter import CurrencyRates

def main():
    print("Moedas disponíveis: " + moedas())

    # Entrada de dados de tipo de moeda à ser convertida
    converteDe   = input("De moeda..........: ")
    convertePara = input("Para moeda........: ")

    # Valor à ser convertido
    quantidade   = input("Quantidade........: ")

    converteMoeda(converteDe, convertePara, int(quantidade))

def converteMoeda(converteDe, convertePara, quantidade):
    converter = CurrencyRates()

    # Converte de uma moeda para outra
    valor = converter.convert(converteDe, convertePara, quantidade)
    print(f"\nValor de {converteDe} {quantidade:,.2f} em {convertePara} {valor:,.2f}")

def moedas():
    # Somente exibe as moedas disponíveis
    return ("USD, JPY, BGN, CZK, DKK, GBP, HUF, PLN, RON, SEK, CHF, ISK, NOK, TRY, AUD, BRL, CAD, CNY, HKD, IDR, INR, "
            "KRW, MXN, MYR, NZD, PHP, SGD,THB, ZAR")

if __name__ == '__main__':
    main()