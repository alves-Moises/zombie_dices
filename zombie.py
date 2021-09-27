# Gustavo Manoel Sampaio - RA:1112021200400.
# Análise e Desenvolvimento de Sistemas. 

jogadores = 0
lista_jogadores = []
dados = ("CPCTPC","CPCTPC","CPCTPC","CPCTPC","CPCTPC","CPCTPC","TPCTPC","TPCTPC","TPCTPC","TPCTP","TPTCPT","TPTCPT","TPTCPT")
cerebros = 0
tiros = 0
passos = 0
import random
import time 
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
            nome_jogadores = input(str(f"Jogador {i+1}, digite seu nome:"))
            lista_jogadores.append(input(f'Jogador {i+1}, digite seu nome: ')))
        time.sleep(1)

def main():
    lin()
    print("Seja bem-vindo ao Zombie Dice.")
    print("Podemos começar?")
    lin()

    while (jogadores < 2):
        print("Quantos jogadores irão participar? Precisamos de no minimo 2 jogadores:")
        jogadores = valida_int()

    

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

