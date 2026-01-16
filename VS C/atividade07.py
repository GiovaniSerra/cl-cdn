#1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  
#e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 


import pandas as pd
import json

arquivo_csv = input("Digite o caminho do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo_csv)

    if "tempo_execucao" not in df.columns:
        print("Erro: a coluna 'tempo_execucao' não existe no CSV.")
    else:
        media = df["tempo_execucao"].mean()
        maximo = df["tempo_execucao"].max()

        print(f"Média de tempo_execucao: {media:.2f}")
        print(f"Máximo de tempo_execucao: {maximo:.2f}")

except FileNotFoundError:
    print("Erro: arquivo CSV não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: o arquivo CSV está vazio ou inválido.")
except Exception:
    print("Erro: falha na leitura do arquivo CSV.")


#2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, 
#que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 


pessoas = [
    {"nome": "Giovani", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Laura", "idade": 28, "cidade": "Campinas"},
    {"nome": "Marina", "idade": 24, "cidade": "São Paulo"},
]

arquivo_txt_saida = input("\nDigite o caminho/nome do arquivo para salvar (ex: pessoas.txt): ")

try:
    with open(arquivo_txt_saida, "w", encoding="utf-8") as f:
        f.write(f"{'Nome':<15}{'Idade':<10}{'Cidade':<20}\n")
        f.write("-" * 45 + "\n")

        for p in pessoas:
            f.write(f"{p['nome']:<15}{p['idade']:<10}{p['cidade']:<20}\n")

    print(f"Arquivo salvo com sucesso em: {arquivo_txt_saida}")

except Exception:
    print("Falha: erro ao salvar o arquivo.")


#3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo 
#e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.

arquivo_txt_leitura = input("\nDigite o caminho do arquivo TXT para ler: ")

try:
    with open(arquivo_txt_leitura, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.rstrip())

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception:
    print("Erro: falha ao ler o arquivo.")


#4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, 
#idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, 
# mostre uma mensagem de falha.import json

arquivo_json = input("\nDigite o caminho/nome do arquivo JSON (ex: dados.json): ")

dados = {
    "nome": "Giovani",
    "idade": 25,
    "cidade": "São Paulo"
}
try:
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print("Dados salvos com sucesso.")

except Exception:
    print("Falha: erro ao salvar o arquivo JSON.")

try:
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    print("\nDados lidos do JSON:")
    print(f"Nome:   {dados_lidos.get('nome', 'N/D')}")
    print(f"Idade:  {dados_lidos.get('idade', 'N/D')}")
    print(f"Cidade: {dados_lidos.get('cidade', 'N/D')}")

except FileNotFoundError:
    print("Falha: arquivo JSON não existe para leitura.")
except json.JSONDecodeError:
    print("Falha: JSON inválido ou corrompido.")
except Exception:
    print("Falha: erro ao ler o arquivo JSON.")