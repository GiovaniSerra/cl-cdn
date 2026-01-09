#1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

#* Valor em reais: R$ 100.00
#* Taxa do dólar: R$ 5.20
#* Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor = 100.00
dolar = 5.20
euro = 6.15
r_dolar = (valor / dolar)
r_euro = (valor / euro)

print(f"O valor de R${valor:.2f} em dolares é de {r_dolar:.2f}, devido a taxa de {dolar} do dolar.\n"
      f"Em euro, é de {r_euro:.2f}, devido a taxa de {euro} do euro")


#2- Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#* Nome do produto: "Camiseta"
#* Preço original: R$ 50.00
#* Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

produto = "Camiseta"
preco = 50.00
desconto = 20
valor_desc = (preco * (desconto/100))
preco_final = preco - valor_desc

print(f"{produto} está em promoção de {desconto}%, de {preco:.2f} por apenas R${preco_final:.2f}, um desconto de R${valor_desc:.2f}!")

#3- Calculadora de Média Escolar
#Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

#* Nota 1: 7.5
#* Nota 2: 8.0
#* Nota 3: 6.5
#O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3)/3

print(f"A media do aluno é de {media:.2f}, sendo as notas de {nota1:.2f}, {nota2:.2f} e {nota3:.2f}")

#4- Calculadora de Consumo de Combustível
#Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

#* Distância percorrida: 300 km
#* Combustível gasto: 25 litros
#O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

distancia = 300
combustivel = 25
media = (distancia / combustivel)

print(f"Com a distancia percorria de {distancia} km e combustivel gasto de {combustivel} litros a media de consumo é de {media:.2f} km/l")