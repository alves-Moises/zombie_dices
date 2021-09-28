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

def verifica_venceu(jogador):
    if jogador['C'] == 13:
        venceu = True
    else:
        venceu = False
    return venceu

def verifica_morte(jogador):
    if jogador['T'] == 3:
        morte = True
    else:
        morte = False
    return morte

def continue_function():
    valid = False
    while not valid:
        x = valida_int()
        if not (x in [1, 2]):
            print('resposta inválida.')
        else:
            continuar = True if (x == 1) else False
    return continuar
        
# def joga_dado(tube, dado):
#     escolha = escolhe_dados(tube)
    
#     escolha = random.choice(dado[escolha])
#     return escolha

    escolha = random.choice(dado[escolha])
    return escolha
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
    i = 0 #rodar só os passos caso existam
    dados_jogando = []  #lista  dados jogados
    while i < 3:
        escolha = escolhe_dados(tube)
        print('Dado escolhido: ', 'Vermelho' if escolha == 'r' else 'Amarelo' if escolha == 'y' else 'Verde')
        dados_jogando.append(random.choice(lista_dados[escolha]))
        i += 1
    return dados_jogando

#inicio do programa
def main():
    #variaveis
    jogadores = 0
    lista_vitoria = []
    lista_derrota = []
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

    game = True
    #looping do jogo
    while game and (lista_jogadores != []):
        info_jogadores[nome]['T'] = 0
        #jogada por jogador 'nome'
        for nome in lista_jogadores:
            dados_jogada = []

            
            jogada = True
            lin()
            print(f'Jogada de {nome}:')
            while jogada:
                dados_jogados = joga_dados(tubo, dados,  dados_jogada) 
                print('Resultado:', dados_jogados)
                print('C: cerebro || T: tiro || P: passos')

                #contabiliza valores
                for dice in dados_jogados:
                    if dice == 'C':
                        info_jogadores[nome]['C'] += 1
                    if dice == 'T':
                        info_jogadores[nome]['T'] += 1

                lin()   #printar informações
                print('Nome: ', nome)
                print('Cérebros: ', info_jogadores[nome]['C'])
                print('Tiros: ', info_jogadores[nome]['T'])
                lin()

                if verifica_venceu(info_jogadores[nome]):
                    print(f'Jogador {nome} venceu.')
                    lista_jogadores.remove(nome)
                    lista_vitoria.append(nome)
                    jogada = False
                    break

                elif verifica_morte(info_jogadores[nome]):
                    print(f'Jogador {nome} perdeu.')
                    lista_jogadores.remove(nome)
                    lista_derrota.append(nome)
                    jogada = False
                
                elif 'C' in dados_jogados:
                        print('Você gostaria de jogar novamente? \n[1] Sim \n[2] Não')
                        jogada = continue_function()
                else:
                        jogada = False
                        input('Digite enter para continuar')
            lin()    
            lin()    
            if lista_jogadores != []:
                print('Próximo jogador: ')
            else: game = False

            #jogada = dados_jogada.append()

    print(info_jogadores)
    lin()
    print('Fim de jogo')
    lin()

    print('Ranking:')

    if not(lista_vitoria == []):
        for i in range(len(lista_vitoria)):
            print(f'Jogador {i+1}: {lista_vitoria[i]} || Cérebros: ', info_jogadores[lista_vitoria[i]]['C'])
        lin()

    if not(lista_derrota == []):
        print('Lista derrota:')
        for i in range(len(lista_derrota)):
            print(f'Jogador {i+1}: {lista_derrota[i]} || Cérebros: ', info_jogadores[lista_derrota[i]]['C'])
        lin()
main()
