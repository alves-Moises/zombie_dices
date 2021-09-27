# Gustavo Manoel Sampaio - RA:1112021200400.
# Análise e Desenvolvimento de Sistemas. 

import random
import time 

#desenha uma linha
def lin():
    print('-=' *30, '\n')

def tubo_func():
    tubo = [
            'g', 'g', 'g', 'g', 'g', 'g',   #verde
            'y', 'y', 'y', 'y',             #amarelo
            'r', 'r', 'r'                   #vermelho
        ]
    return tubo

def dados_func():
    dados = {
            'g': [
                'C', 'C', 'C',
                'P', 'P',
                'T'
            ],
            'y': [
                'C', 'C',
                'P', 'P',
                'Y', 'Y'
            ],
            'r': [
                'C',
                'P', 'P',
                'T', 'T', 'T', 
            ]
    }
    return dados

def boas_vindas():
    lin()
    print("Seja bem-vindo ao Zombie Dice.")
    print("Podemos começar?")
    lin()

def continue_function():
    valid = False
    while not valid:
        x = valida_int()
        if not (x in [1, 2]):
            print('resposta inválida.')
        else:
            continuar = True if (x == 1) else False
    return continuar
        
def joga_dado(tube, dado):
    escolha = escolhe_dados(tube)

#valida valor inteiro de entrada
def valida_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('Digite um valor válido')
        else:
            valid = True
    return x

def nomes(i):
    for j in range(i):
        lista_jogadores.append(input(f'Jogador {j+1}, digite seu nome: '))
        time.sleep(0.5)
    return lista_jogadores

def listar_jogadores():
    print('Digite o total de jogadores: (minimo 2 jogadores)')
    valid = False
    while not valid:
        x = valida_int()
        if x < 2:
            print('A quantidade minima é de 2 jogadores.')
        else:
            valid = True
    return x

#escolhe um dado do tubo
def escolhe_dados(tube):
    return random.choice(tube)

def joga_dados(tube, lista_dados, dados_passos = []):
    i = 3 - len(dados_passos) #rodar só os passos caso existam
    dados_jogando = []  #lista  dados jogados
    while i < 3:
        escolha = escolhe_dados(lista_dados)
        dados_jogando.append(random.choice(tube[escolha]))
        i += 1
    print(dados_jogando)

def main():
    #variaveis
    jogadores = 0
    lista_jogadores = []
    info_jogadores = {}
    
    tubo = tubo_func()

    dados = dados_func()

    #info
        #pontuação
        # cerebros = 0
        # tiros = 0
        # passos = 0

    boas_vindas()
    #definir nomes e total de jogadores
    lista_jogadores = nomes(listar_jogadores())

    #definir atributos zerados a cada jogador
    for nome in lista_jogadores:
        info_jogadores[f'{nome}'] = {'C':0, 'T':0, 'P':0}

    while (jogadores < 2):
        print("Quantos jogadores irão participar? Precisamos de no minimo 2 jogadores:")
        jogadores = valida_int()

        #jogada por jogador 'nome'
        for nome in lista_jogadores:
            dados_jogada = []

            info_jogadores[nome]['T'] = 0
            jogada = True
            dados_jogada = []
            while jogada:
                dados_jogados = joga_dados(tubo, dados,  dados_jogada) 
                print(dados_jogados)
                print('Você gostaria de continuar? \n[1] Sim \n[2] Não')
                jogada = continue_function()

    for d in range(0,3):
        dado = random.choice(dados)
        face = random.choice(face)
        print(f"Jogador {i} seu dado é {dado}, e a face é {face}!")
        lin()
            
        if face == "C":
            cerebros = cerebros + 1
        elif face == "T":
            tiros = tiros + 1
        elif face == "P":
            passos = passos + 1
        time.sleep(1)
        lin()
    print(f"Cerebros = {cerebros}, Passos = {passos}, Tiros = {tiros}")

