# Example file showing a basic pygame "game loop"
import pygame # importação da biblioteca pygame
import random

# pygame setup
pygame.init() # inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame
screen = pygame.display.set_mode((600, 600)) # tamanho da tela utilizada

pygame.display.set_caption("Jogo da Velha") # coloca o nome (título) da tela
clock = pygame.time.Clock() # biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont("Comic Sans Ms", 100) #importar fonte
running = True # variável de controle de status do jogo

personagem_x = fonte_quadrinhos.render("X", True, "red")
personagem_o = fonte_quadrinhos.render("O", True, "blue")
mensagem_final = fonte_quadrinhos.render("Game Over", True, "red", "black")
jogador_atual = personagem_x
x_ganhou = "Jogador X venceu"
o_ganhou = "Jogador O venceu"
rodadas = 0
tabuleiro_desenhado = False

coordenada_x = 0
coordenada_y = 0

espessura = 1
cores = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Pink", "Gray", "Brown", "Cyan", "Magenta", "Gold", "Silver"]
cor_tabuleiro = random.choice(cores)
quadrante = ["", "", "", "", "", "", "", "", ""]

def tabuleiro(espessura, cor_tabuleiro):
     # desenha tabuleiro    
                 #                          origem     destino
                 #                          (x, y)     (x, y)    
    pygame.draw.line(screen, cor_tabuleiro, (200, 0), (200, 600), espessura)
    pygame.draw.line(screen, cor_tabuleiro, (400, 0), (400, 600), espessura)
    pygame.draw.line(screen, cor_tabuleiro, (0, 200), (600, 200), espessura)
    pygame.draw.line(screen, cor_tabuleiro, (0, 400), (600, 400), espessura)

def faz_jogada():
    global rodadas
    global jogador_atual
    if rodadas != 1:
        if jogador_atual == personagem_x:
            jogador_atual = personagem_o
        else:
            jogador_atual = personagem_x
    else:
        jogador_atual = personagem_x

    if posicao[0] <=200 and posicao[1] <200:
        screen.blit(jogador_atual, (60, 30)) # primeiro
        quadrante[0] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >=200 and posicao[0] <400 and posicao[1] <200:
        screen.blit(jogador_atual, (260, 30)) # segundo
        quadrante[1] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >400 and posicao[1] <=200:
        screen.blit(jogador_atual, (460, 30)) # terceiro
        quadrante[2] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] <200 and posicao[1] >200 and posicao[1] <400:
        screen.blit(jogador_atual, (60, 230)) # quarto
        quadrante[3] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >=200 and posicao and posicao[0] <400 and posicao[1] >200 and posicao[1] <400:
        screen.blit(jogador_atual, (260, 230)) # quinto
        quadrante[4] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >400 and posicao[1] >=200 and posicao[1] <400:
        screen.blit(jogador_atual, (460, 230)) # sexto
        quadrante[5] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] <200 and posicao[1] >=400:
        screen.blit(jogador_atual, (60, 430)) # sétimo
        quadrante[6] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >=200 and posicao[0] <400 and posicao[1] >=400:
        screen.blit(jogador_atual, (260, 430)) # oitavo
        quadrante[7] = "X" if jogador_atual == personagem_x else "O"

    elif posicao[0] >=400 and posicao[1] >=400:
        screen.blit(jogador_atual, (460, 430)) # nono
        quadrante[8] = "X" if jogador_atual == personagem_x else "O"

def descobrir_ganhador():

    if quadrante[0] == "" or quadrante[1] == "" or quadrante[3] == "" or quadrante[4] == "" or quadrante[5] == "" or quadrante[6] == "" or quadrante[7] == "" or quadrante[8] == "":
        print("quadrante vazio")
 
    # lógica 1 (ganhadores horizontais)
    
    elif quadrante[0] == quadrante[1] and quadrante[1] == quadrante[2]:
        if quadrante[0] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)

    elif quadrante[3] == quadrante[4] and quadrante[4] == quadrante[5]:
        if quadrante[3] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)

    elif quadrante[6] == quadrante[7] and quadrante[7] == quadrante[8]:
        if quadrante[6] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)

    # lógica 2 (ganhadores laterais)

    elif quadrante[0] == quadrante[3] and quadrante[3] == quadrante[6]:
        if quadrante[0] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)
    
    elif quadrante[1] == quadrante[4] and quadrante[4] == quadrante[7]:
        if quadrante[1] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)
    elif quadrante[2] == quadrante[5] and quadrante[5] == quadrante[8]:
        if quadrante[2] == "X":
            print(x_ganhou)
        else:
            print(o_ganhou)



while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicou")
            posicao = pygame.mouse.get_pos()
            print("Eixo X", posicao[0]) # Eixo X
            print("Eixo Y", posicao[1]) # Eixo Y
            rodadas = rodadas + 1
            faz_jogada()
            descobrir_ganhador()
            if rodadas >= 10:
                screen.fill("black")
                tabuleiro_desenhado = False
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                tabuleiro(espessura, cor_tabuleiro)

    if tabuleiro_desenhado == False:
        tabuleiro(espessura, cor_tabuleiro)  
        tabuleiro_desenhado = True

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60          
pygame.quit()