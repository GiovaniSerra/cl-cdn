#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

print("Calculadora Simples")
num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("\nDigite a opção desejada (1/2/3/4): ")

if opcao == "1":
    print(f"Resultado da soma: {soma(num1, num2)}")
elif opcao == "2":
    print(f"Resultado da subtração: {subtracao(num1, num2)}")
elif opcao == "3":
    print(f"Resultado da multiplicação: {multiplicacao(num1, num2)}")
elif opcao == "4":
    print(f"Resultado da divisão: {divisao(num1, num2)}")
else:
    print("Opção inválida.")

#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

notas = []
while True:
    nota = input("\nDigite uma nota (ou 'fim' para encerrar): ")
    if nota.strip().lower() in ("fim", "f"):
        break
    try:
        notas.append(float(nota))
    except ValueError:
        print("\nNota inválida. Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nA média da turma é: {media}")
else:
    print("\nNenhuma nota foi registrada.")




#3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança..
#   a - deve ter pelo menos 8 caracteres.
#   b - deve conter pelo menos um número.

senha = input("\nDigite uma senha: ")
if len(senha) >= 8 and any(c.isdigit() for c in senha):
    print("\nSenha válida.")
else:
    print("\nSenha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")





#4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

pares = 0
impares = 0

while True:
    entrada = input("\nDigite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"\nNúmero {numero} é par.")
        else:
            impares += 1
            print(f"\nNúmero {numero} é ímpar.")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.")