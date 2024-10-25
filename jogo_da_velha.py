# Example file showing a basic pygame "game loop"
import pygame # importação da biblioteca pygame

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
rodadas = 0

coordenada_x = 0
coordenada_y = 0

quadrante_1 = 0
quadrante_2 = 0
quadrante_3 = 0
quadrante_4 = 0
quadrante_5 = 0
quadrante_6 = 0
quadrante_7 = 0
quadrante_8 = 0
quadrante_9 = 0


while running:
    # desenha tabuleiro    
            #                          origem     destino
            #                          (x, y)     (x, y)    
    pygame.draw.line(screen, "white", (200, 0), (200, 600), 1)
    pygame.draw.line(screen, "white", (400, 0), (400, 600), 1)
    pygame.draw.line(screen, "white", (0, 200), (600, 200), 1)
    pygame.draw.line(screen, "white", (0, 400), (600, 400), 1)
    
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
            print(rodadas)
            
            if rodadas != 1:
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
            else:
                jogador_atual = personagem_x

            if posicao[0] <=200 and posicao[1] <200:
                screen.blit(jogador_atual, (60, 30)) # primeiro

            elif posicao[0] >=200 and posicao[0] <400 and posicao[1] <200:
                screen.blit(jogador_atual, (260, 30)) # segundo

            elif posicao[0] >400 and posicao[1] <=200:
                screen.blit(jogador_atual, (460, 30)) # terceiro
                quadrante_3 = jogador_atual

            elif posicao[0] <200 and posicao[1] >200 and posicao[1] <400:
                screen.blit(jogador_atual, (60, 230)) # quarto
                quadrante_4 = jogador_atual

            elif posicao[0] >=200 and posicao and posicao[0] <400 and posicao[1] >200 and posicao[1] <400:
                screen.blit(jogador_atual, (260, 230)) # quinto
                quadrante_5 = jogador_atual

            elif posicao[0] >400 and posicao[1] >=200 and posicao[1] <400:
                screen.blit(jogador_atual, (460, 230)) # sexto
                quadrante_6 = jogador_atual

            elif posicao[0] <200 and posicao[1] >=400:
                screen.blit(jogador_atual, (60, 430)) # sétimo
                quadrante_7 = jogador_atual

            elif posicao[0] >=200 and posicao[0] <400 and posicao[1] >=400:
                screen.blit(jogador_atual, (260, 430)) # oitavo
                quadrante_8 = jogador_atual

            elif posicao[0] >=400 and posicao[1] >=400:
                screen.blit(jogador_atual, (460, 430)) # nono
                quadrante_9 = jogador_atual
   
            if rodadas >= 10:
                screen.fill("black")
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60          
pygame.quit()