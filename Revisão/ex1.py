import random

def embaralhar_palavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

def jogar():
    palavras = ['python', 'algoritmo', 'programacao', 'desafio', 'otimizacao']
    palavra_secreta = random.choice(palavras)
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)

    tentativas_restantes = 5
    palavras_animo = [
        "Você consegue!", "Não desista!", "Tente mais uma vez!", "Você está quase lá!", "Continue firme!"
    ]

    print("Bem-vindo ao jogo de adivinhar palavras!")
    print(f"A palavra embaralhada é: {palavra_embaralhada}")

    while tentativas_restantes > 0:
        tentativa = input(f"Qual é a palavra? ({tentativas_restantes} tentativas restantes): ")

        if tentativa.lower() == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra '{palavra_secreta}'!")
            print(f"Você utilizou {5 - tentativas_restantes + 1} tentativas.")
            break
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(random.choice(palavras_animo))
    
    if tentativas_restantes == 0:
        print(f"Suas tentativas acabaram. A palavra correta era '{palavra_secreta}'.")

# Executa o jogo
jogar()
