import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")
    print(f"Você tem {max_tentativas} tentativas.\n")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Adivinhe o número (entre 1 e 100): "))
            if palpite < 1 or palpite > 100:
                print("Por favor, insira um número entre 1 e 100.")
                continue
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.\n")

    if palpite != numero_secreto:
        print(f"Que pena! O número correto era {numero_secreto}.")

if __name__ == "__main__":
    jogar()