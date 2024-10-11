# Example file showing a basic pygame "game loop"
import pygame # importação da biblioteca pygame

# pygame setup
pygame.init() # inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame
screen = pygame.display.set_mode((500, 500)) # tamanho da tela utilizada
pygame.display.set_caption("Jogo da Velha") # coloca o nome (título) da tela
clock = pygame.time.Clock() # biblioteca de tempo
fonte_quadrinhos = pygame.font.SysFont("Comic Sans Ms", 30) #importar fonte
running = True # variável de controle de status do jogo
personagem_x = fonte_quadrinhos.render("X", True, "red")
personagem_y = fonte_quadrinhos.render("O", True, "green")
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
            if(cor_fundo > 3):
                cor_fundo = 1
 
    if cor_fundo == 1:
        screen.fill("black")
        screen.blit(personagem_x, (250, 250))
    elif cor_fundo == 2:
        screen.fill("black")
        screen.blit(personagem_y, (250, 250))
    else:
        screen.fill("yellow")
        
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()