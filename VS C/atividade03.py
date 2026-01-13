#1- Classificador de Idade

#Crie um programa que solicite a idade do usuário e classifique-o
#em uma das seguintes categorias:

#*Criança (0-12 anos),
#*Adolescente (13-17 anos),
#*Adulto (18-59 anos) ou
#*Idoso (60 anos ou mais).

try:
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Você é uma criança.")
    elif idade <= 17:
        print("Você é um adolescente.")
    elif idade <= 59:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")

except ValueError:
    print("Idade inválida. Digite apenas números inteiros.")


#2- Calculadora de IMC

#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

#< 18.5: classificacao = "Abaixo do peso"
#< 25: classificacao = "Peso normal"
#< 30: classificacao = "Sobrepeso"
#Para os demais cenários: classificacao = "Obeso"


try:
    peso = float(input("\nDigite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if peso <= 0 or altura <= 0:
        print("Peso ou altura inválidos.")
    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print(f"Seu IMC é {imc:.2f}")
        print(f"categoria: {classificacao}")

except ValueError:
    print("Erro: digite apenas números válidos.")


#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


try:
    temperatura = float(input("\nDigite a temperatura: "))
except ValueError:
    print("Temperatura inválida.")
    temperatura = None
if temperatura is not None:
    unidade_origem = input("Unidade de origem (C, F, K): ").strip().lower()
    unidade_destino = input("Unidade de destino (C, F, K): ").strip().lower()

    if unidade_origem == unidade_destino:
        resultado = temperatura

    elif unidade_origem == "c":
        if unidade_destino == "f":
            resultado = (temperatura * 9/5) + 32
        elif unidade_destino == "k":
            resultado = temperatura + 273.15
        else:
            resultado = None

    elif unidade_origem == "f":
        if unidade_destino == "c":
            resultado = (temperatura - 32) * 5/9
        elif unidade_destino == "k":
            resultado = (temperatura - 32) * 5/9 + 273.15
        else:
            resultado = None

    elif unidade_origem == "k":
        if unidade_destino == "c":
            resultado = temperatura - 273.15
        elif unidade_destino == "f":
            resultado = (temperatura - 273.15) * 9/5 + 32
        else:
            resultado = None

    else:
        resultado = None

    if resultado is not None:
        print(f"\n Dado a temperatura de {temperatura} em {unidade_origem}, a temperatura convertida é: {resultado:.2f}° {unidade_destino}.")
    else:
        print("\nErro na conversão. Verifique as unidades informadas.")


#4- Verificador de Ano Bissexto

#Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
#Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

try:
    ano = int(input("\n Digite um ano para verificar se é bissexto: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"\n O ano de {ano} é bissexto.")
    else:
        print(f"\n O ano de {ano} não é bissexto.")

except ValueError:
    print("Ano inválido. Por favor, insira um número inteiro válido.")