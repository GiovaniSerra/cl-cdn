#parte 1 = 
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é uma criança")
elif idade < 18:
    print("Você é um adolescente")
elif idade < 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# parte 2 = Usando lambda

verificar_resultado = lambda nota: "Aprovado" if nota >= 6 else "reprovado"

nota = float(input("Digite a nota do aluno: "))
print (verificar_resultado(nota))

#parte 3 - usando função

def verificar_resultado(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"
    
nota = float(input("Digite a nota do aluno: "))
print(verificar_resultado(nota))