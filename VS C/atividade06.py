#1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  
#também escolha o tamanho da senha  para criar senhas seguras automaticamente.

import string
import secrets

def gerar_senha(tamanho: int) -> str:
    if tamanho < 6:
        raise ValueError("O tamanho mínimo recomendado é 6.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Digite o tamanho da senha: "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
except ValueError as e:
    print(f"Falha: {e}")


#2 - Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. 
#exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

import requests

def buscar_usuario_aleatorio() -> dict:
    url = "https://randomuser.me/api/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    user = data["results"][0]
    nome = f'{user["name"]["first"]} {user["name"]["last"]}'
    email = user["email"]
    pais = user["location"]["country"]

    return {"nome": nome, "email": email, "pais": pais}

try:
    u = buscar_usuario_aleatorio()
    print("Usuário aleatório:")
    print(f"Nome:  {u['nome']}")
    print(f"E-mail: {u['email']}")
    print(f"País:  {u['pais']}")
except requests.RequestException:
    print("Falha: erro na conexão ou na requisição da API.")
except (KeyError, IndexError, ValueError):
    print("Falha: resposta da API em formato inesperado.")



#3 - Crie um programa que consulte informações de um  na API , retorne logradouro, 
#bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.



import requests

def consultar_cep(cep: str) -> dict:
    cep_numeros = "".join(ch for ch in cep if ch.isdigit())

    if len(cep_numeros) != 8:
        raise ValueError("CEP inválido: deve conter 8 dígitos.")

    url = f"https://viacep.com.br/ws/{cep_numeros}/json/"
    resp = requests.get(url, timeout=10)

    resp.raise_for_status()

    data = resp.json()

    if data.get("erro") is True:
        raise ValueError("CEP não encontrado.")

    if "localidade" not in data or "uf" not in data:
        raise ValueError("Resposta da API em formato inesperado.")

    return {
        "logradouro": data.get("logradouro", "N/D"),
        "bairro": data.get("bairro", "N/D"),
        "cidade": data.get("localidade", "N/D"),
        "estado": data.get("uf", "N/D"),
    }

try:
    cep_in = input("Digite o CEP (ex: 01001-000 ou 01001000): ")
    info = consultar_cep(cep_in)

    print("\nEndereço encontrado:")
    print(f"Logradouro: {info['logradouro']}")
    print(f"Bairro:     {info['bairro']}")
    print(f"Cidade:     {info['cidade']}")
    print(f"Estado:     {info['estado']}")

except ValueError as e:
    print(f"Falha: {e}")

except requests.RequestException:
    print("Falha: erro na conexão ou na requisição da API.")

#4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, 
#máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests
from datetime import datetime

def consultar_cotacao(par_moeda: str) -> dict:
    par_moeda = par_moeda.strip().upper()

    if "-" not in par_moeda or len(par_moeda.split("-")[0]) < 3:
        raise ValueError("Informe no formato USD-BRL, EUR-BRL, BTC-BRL, etc.")

    url = f"https://economia.awesomeapi.com.br/json/last/{par_moeda}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    chave = par_moeda.replace("-", "")
    if chave not in data:
        raise ValueError("Moeda/par não encontrado na API.")

    c = data[chave]

    atual = float(c["bid"])
    maxima = float(c["high"])
    minima = float(c["low"])
    ultima_atualizacao = c.get("create_date")

    if not ultima_atualizacao and "timestamp" in c:
        ultima_atualizacao = datetime.fromtimestamp(int(c["timestamp"])).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "par": par_moeda,
        "atual": atual,
        "maxima": maxima,
        "minima": minima,
        "ultima_atualizacao": ultima_atualizacao or "N/D",
    }

try:
    par = input("Digite o par de moedas (ex: USD-BRL): ")
    cot = consultar_cotacao(par)
    print(f"Cotação {cot['par']}:")
    print(f"Valor atual: R$ {cot['atual']:.4f}")
    print(f"Máxima:      R$ {cot['maxima']:.4f}")
    print(f"Mínima:      R$ {cot['minima']:.4f}")
    print(f"Atualização: {cot['ultima_atualizacao']}")
except ValueError as e:
    print(f"Falha: {e}")
except requests.RequestException:
    print("Falha: erro na conexão ou na requisição da API.")
except (KeyError, TypeError):
    print("Falha: resposta da API em formato inesperado.")