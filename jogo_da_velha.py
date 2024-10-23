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
personagem_y = fonte_quadrinhos.render("O", True, "green")
mensagem_final = fonte_quadrinhos.render("Game Over", True, "red", "black")
personagem = 0


while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            print("Eixo X", posicao[0]) # Eixo X
            print("Eixo Y", posicao[1]) # Eixo Y
            print("Clicou")
            personagem = personagem + 1
            if personagem == 10:
                screen.fill("black")
                screen.blit(mensagem_final, (50, 200))
            else:
                if personagem == 0:
                    screen.fill()
                elif posicao[0] <=200 and posicao[1] <200:
                    screen.blit(personagem_x, (60, 30)) # primeiro

                elif posicao[0] >=200 and posicao[0] <400 and posicao[1] <200:
                    screen.blit(personagem_y, (260, 30)) # segundo

                elif posicao[0] >400 and posicao[1] <=200:
                    screen.blit(personagem_x, (460, 30)) # terceiro

                elif posicao[0] <200 and posicao[1] >200 and posicao[1] <400:
                    screen.blit(personagem_y, (60, 230)) # quarto

                elif posicao[0] >=200 and posicao and posicao[0] <400 and posicao[1] >200 and posicao[1] <400:
                    screen.blit(personagem_x, (260, 230)) # quinto

                elif posicao[0] >400 and posicao[1] >=200 and posicao[1] <400:
                    screen.blit(personagem_y, (460, 230)) # sexto

                elif posicao[0] <200 and posicao[1] >=400:
                    screen.blit(personagem_x, (60, 430)) # sétimo

                elif posicao[0] >=200 and posicao[0] <400 and posicao[1] >=400:
                    screen.blit(personagem_y, (260, 430)) # oitavo

                elif posicao[0] >=400 and posicao[1] >=400:
                    screen.blit(personagem_x, (460, 430)) # nono

                if personagem > 10:
                    personagem = 0

    # desenha tabuleiro    
    #                                  origem     destino
    #                                  (x, y)     (x, y)    
    pygame.draw.line(screen, "white", (200, 0), (200, 600), 1)
    pygame.draw.line(screen, "white", (400, 0), (400, 600), 1)
    pygame.draw.line(screen, "white", (0, 200), (600, 200), 1)
    pygame.draw.line(screen, "white", (0, 400), (600, 400), 1)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()