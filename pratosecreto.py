"""Objetivo: Adivinhar o prato secreto(Comida) escolhido pelo computador a partir de uma lista de opções.

Instruções para os Alunos:
Obs: Utilize listas

1.Lista de Pratos: O programa terá uma lista predefinida de pratos deliciosos.
2.Escolha Aleatória: O computador escolherá aleatoriamente um prato dessa lista como o prato secreto.
3.Número de Tentativas: O jogador terá um número limitado de tentativas para adivinhar o prato secreto (por exemplo, 5 tentativas).
4.Adivinhação: O programa pedirá ao jogador para digitar sua tentativa de prato.
5.Verificação: O programa comparará a tentativa do jogador com o prato secreto.
6.Resultado:
-Se o jogador acertar, o programa exibirá uma mensagem de parabéns.
-Se o jogador errar, o programa informará que a tentativa está incorreta e dirá quantas tentativas restam.
-Se as tentativas acabarem, o programa mostrará o prato secreto.
Entrega: A entrega deverá ser feita pelo github
"""
import random
print(18*"-")
print("|Descubra o prato secreto!|")
print(18*"-")

#Lista de Pratos e Escolha Aleatória
pratos = ["macarrao", "lasanha", "strogonof", "bacalhau", "pizza", "hamburguer", "parmegiana", "japones", "feijoada", "mexicano", "chines","churrasco"]
print(f"As opções para o prato secreto são:{pratos}")
prato_secreto = random.choice(pratos) # o random.choice(list) gera um elemento aleatório de uma lista


#Número de tentativas, Adivinhação 
max_tentativas = 5
acertou = False

for tentativas in range(1,max_tentativas+1):
    print(f"\nTentativa {tentativas} de {max_tentativas}")
    palpite = str(input("Informe seu palpite sobre qual é o prato secreto: ")).lower()

#Verificação e Resultado
    if palpite == prato_secreto:
        print(f"Parabéns!!Você acertou o prato secreto!")
        acertou = True
        break
    else:
        tentativas_restantes = max_tentativas - tentativas
        
        if tentativas_restantes>0:
            print(f"Tentativa incorreta, não desita! Ainda restam {tentativas_restantes}")
        else:
            print("Última tentativa está errada! Fim de jogo!")
print(f"O prato secreto é: {prato_secreto}")
