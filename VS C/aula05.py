# Programa para verificar a cotação do dólar americano em relação ao real brasileiro em tempo real

import requests

converter_para_real = lambda valor, cotacao: valor * cotacao

def obter_cotacao_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        if "USDBRL" in dados:
            cotacao_dolar = float(dados["USDBRL"]["bid"])
            return cotacao_dolar
        
        else:
            print("Erro ao obter a cotação do dólar.")
            return None
        
    except requests.exceptions.RequestException:
        print("Erro ao conectar à API.")
        return None

def main():
    try:
        valor_dolar = float(input("Digite o valor em dólares (USD) que deseja converter para reais (BRL): "))

        cotacao = obter_cotacao_dolar()

        if cotacao:
            valor_real = converter_para_real(valor_dolar, cotacao)
            print(f"\n O valor de {valor_dolar:.2f} USD convertido para BRL é R$ {valor_real:.2f} devido a cotação atual de R$ {cotacao:.2f} por dólar.")
        
        else:
            print("Não foi possível realizar a conversão devido a erro na cotação.")

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        
main()
