#1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
#gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
#Parâmetros:
#a - valor_conta (float): O valor total da conta
#b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
#c - retorna: float: O valor da gorjeta calculada

valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")

#2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

import string

def eh_palindromo(texto):
    texto = texto.lower()
    texto_limpo = ""
    
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim, é um palíndromo"
    else:
        return "Não, não é um palíndromo"

texto = input("Digite uma palavra ou frase: ")
print(eh_palindromo(texto))


#3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
#a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
#b - Preço final: Determina o novo preço após o desconto.
#c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
#d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

preco = float(input("Digite o preço original do produto: R$ "))
desconto_percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

desconto_valor = preco * (desconto_percentual / 100)
preco_final = preco - desconto_valor

print(
    f"O preço final após o desconto é: R$ {preco_final:.2f}. "
    f"Desconto aplicado: R$ {desconto_valor:.2f}. "
    f"Preço original: R$ {preco:.2f}."
)

#4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_atual = datetime.now()
dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")