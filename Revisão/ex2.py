import random

def embaralhar_palavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

def escolher_tema():
    temas = {
        1: 'Cidades',
        2: 'Cores',
        3: 'Times',
        4: 'Países',
        5: 'Objetos'
    }

    print("Escolha um tema:")
    for key, value in temas.items():
        print(f"{key}: {value}")

    escolha = int(input("Digite o número correspondente ao tema desejado: "))
    return temas.get(escolha, 'Cidades')

def escolher_nivel():
    niveis = {
        1: 'Iniciante',
        2: 'Intermediário',
        3: 'Avançado'
    }

    print("Escolha um nível de dificuldade:")
    for key, value in niveis.items():
        print(f"{key}: {value}")

    escolha = int(input("Digite o número correspondente ao nível desejado: "))
    return escolha

def selecionar_palavra(tema, nivel):
    palavras_temas = {
        'Cidades': ['rio', 'paris', 'tokyo', 'londres', 'madrid'],
        'Cores': ['vermelho', 'azul', 'amarelo', 'verde', 'laranja'],
        'Times': ['flamengo', 'barcelona', 'liverpool', 'juventus', 'psg'],
        'Países': ['brasil', 'argentina', 'franca', 'alemanha', 'japao'],
        'Objetos': ['computador', 'telefone', 'relógio', 'caderno', 'mesa']
    }

    # Ajusta o tamanho da palavra de acordo com o nível de dificuldade
    palavras_filtradas = [
        palavra for palavra in palavras_temas[tema]
        if (nivel == 1 and len(palavra) <= 5) or
           (nivel == 2 and 5 < len(palavra) <= 7) or
           (nivel == 3 and len(palavra) > 7)
    ]
    
    return random.choice(palavras_filtradas) if palavras_filtradas else random.choice(palavras_temas[tema])

def jogar():
    tema = escolher_tema()
    nivel = escolher_nivel()

    palavra_secreta = selecionar_palavra(tema, nivel)
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)

    tentativas_restantes = 5
    palavras_animo = [
        "Você consegue!", "Não desista!", "Tente mais uma vez!", "Você está quase lá!", "Continue firme!"
    ]

    print(f"\nVocê escolheu o tema: {tema} e o nível de dificuldade: {['Iniciante', 'Intermediário', 'Avançado'][nivel-1]}")
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
