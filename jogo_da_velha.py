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

# variáveis para desenhar o x e o na tela
mensagem_x_ganhou = "Jogador X ganhou"
mensagem_o_ganhou = "Jogador O ganhou"
fonte_ganhador = pygame.font.SysFont("Arial", 80)
ganhador_x_tela = fonte_ganhador.render(mensagem_x_ganhou, 1, "red")
ganhador_o_tela = fonte_ganhador.render(mensagem_o_ganhou, 1, "blue")

# variáveis para definir personagem atual
jogador_atual = personagem_x
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
    status = False
    
    if quadrante[0] == quadrante[1] == quadrante[2] != "":
        if quadrante[0] == "X":
            pygame.draw.line(screen, "white", (50, 100), (550, 100), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (50, 100), (550, 100), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True

    elif quadrante[3] == quadrante[4] == quadrante[5] != "":
        if quadrante[3] == "X":
            pygame.draw.line(screen, "white", (50, 300), (550, 300), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (50, 300), (550, 300), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True

    elif quadrante[6] == quadrante[7] == quadrante[8] != "":
        if quadrante[6] == "X":
            pygame.draw.line(screen, "white", (50, 500), (550, 500), 10)
            screen.blit(ganhador_x_tela, (30, 190))

            status = True
        else:
            pygame.draw.line(screen, "white", (50, 500), (550, 500), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True

    # lógica 2 (ganhadores verticais)

    elif quadrante[0] == quadrante[3] == quadrante[6] != "":
        if quadrante[0] == "X":
            pygame.draw.line(screen, "white", (100, 50), (100, 550), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (100, 50), (100, 550), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True
    
    elif quadrante[1] == quadrante[4] == quadrante[7] != "":
        if quadrante[1] == "X":
            pygame.draw.line(screen, "white", (300, 50), (300, 550), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (300, 50), (300, 550), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True

    elif quadrante[2] == quadrante[5] == quadrante[8] != "":
        if quadrante[2] == "X":
            pygame.draw.line(screen, "white", (500, 50), (500, 550), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (500, 50), (500, 550), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True

    # lógica 3 (ganhadores diagonais)

    elif quadrante[0] == quadrante[4] == quadrante[8] != "":
        if quadrante[0] == "X":
            pygame.draw.line(screen, "white", (50, 50), (550, 550), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            pygame.draw.line(screen, "white", (50, 50), (550, 550), 10)
            screen.blit(ganhador_o_tela, (30, 190))
            status = True
    elif quadrante[2] == quadrante[4] == quadrante[6] != "":
        if quadrante[2] == "X":
            pygame.draw.line(screen, "white", (550, 50), (50, 550), 10)
            screen.blit(ganhador_x_tela, (30, 190))
            status = True
        else:
            screen.blit(ganhador_o_tela, (30, 190))
            status = True
    return status

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            print(rodadas)
            rodadas = rodadas + 1
            tabuleiro(espessura, cor_tabuleiro)
            faz_jogada()
            descobrir_ganhador()
            
            if rodadas >= 9:
                screen.fill("black")
                tabuleiro_desenhado = False
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                quadrante = ["", "", "", "", "", "", "", "", ""]
                cor_tabuleiro = random.choice(cores)
                tabuleiro(espessura, cor_tabuleiro)

            if (descobrir_ganhador()):
                rodadas = 9

    if tabuleiro_desenhado == False:
        tabuleiro(espessura, cor_tabuleiro)
        tabuleiro_desenhado = True

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60          
pygame.quit()