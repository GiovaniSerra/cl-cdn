tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        resultado = num1 / num2
        print("Resultado da divisão: ", resultado)
        break #sai do loop
    except ValueError: 
        tentativas += 1
        print(f"Erro: digite apenas numeros. Tentativas {tentativas}/3\n") 

    except ZeroDivisionError:
        tentativas += 1
        print(f"Erro: não é possivel dividir por zero. Tentativa {tentativas}/3\n")

    finally:
        if tentativas == max_tentativas:
            print(f"Erro: numero maximo de tentativas atingido. Encerrando o programa")
    

