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
mensagem_final = fonte_quadrinhos.render("Game Over", True, "red")
cor_fundo = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicou")
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 10):
                cor_fundo = 1
    # desenha tabuleiro
    pygame.draw.line(screen, "white", (200, 0), (200, 600), 10)
    pygame.draw.line(screen, "white", (400, 0), (400, 600), 10)
    pygame.draw.line(screen, "white", (0, 200), (600, 200), 10)
    pygame.draw.line(screen, "white", (0, 400), (600, 400), 10)


    if cor_fundo == 1:
        screen.blit(personagem_x, (75, 50))
    elif cor_fundo == 2:
        screen.blit(personagem_y, (250, 50))
    elif cor_fundo == 3:
        screen.blit(personagem_x, (450, 50))
    elif cor_fundo == 4:
        screen.blit(personagem_y, (75, 230))
    elif cor_fundo == 5:
        screen.blit(personagem_x, (250, 230))
    elif cor_fundo == 6:
        screen.blit(personagem_y, (440, 230))
    elif cor_fundo == 7:
        screen.blit(personagem_x, (75, 420))
    elif cor_fundo == 8:
        screen.blit(personagem_y, (250, 420))
    elif cor_fundo == 9:
        screen.blit(personagem_x, (450, 420))
    elif cor_fundo == 10:
        screen.blit(mensagem_final, (50, 300))


    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()