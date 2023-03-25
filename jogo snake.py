#jogo snake.

#importando a biblioteca.
import pygame
from pygame.locals import *
from sys import exit
from random import randint

#criando a janela do jogo
pygame.init()

#música do jogo+colisão

pygame.mixer.music.set_volume(0.55)
musica_de_fundo=pygame.mixer.music.load('boss-133663.mp3')
pygame.mixer.music.play(-1)

barulho_colisao=pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(1)

#tela do jogo

largura_tela=640
altura_tela=480

velocidade=10
x_controle=velocidade
y_controle=0

x_cobra=int(largura_tela//2)    #variável x,y para fazer o objeto se mexer
y_cobra=int(altura_tela//2)

x_maca= randint(40,600)
y_maca= randint(50,430)

pontos=0
fonte=pygame.font.SysFont('gabriola',40,bold=True,italic=True)

tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('jogo snake')
relogio= pygame.time.Clock() #está relacionado ao tempo do objeto se mexendo(fazendo ele cair infinitamente)comprimento_inicial=5
lista_cobra=[]
comprimento_inicial=5
over=False

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela,(0,100,0),(xey[0],xey[1],13,13))

def reiniciar_jogo():
    global pontos,comprimento_inicial,x_cobra,y_cobra,lista_cobra,lista_cabeca,x_maca,y_maca,over
    pontos=0
    comprimento_inicial=5
    x_cobra=int(largura_tela/2)#variável x,y para fazer o objeto se mexer
    y_cobra=int(altura_tela/2)
    lista_cobra=[]
    lista_cabeca=[]
    x_maca= randint(40,600)
    y_maca= randint(50,430)
    over=False
    
while True:
    relogio.tick(30)  #está relacionado ao tempo do objeto se mexendo 
    tela.fill((100,255,0)) #deixa o fundo se q o objeto preenchar todo o fundo
    mensagem=(f'pontos:{pontos}')
    texto_formato=fonte.render(mensagem,False,(0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()     
            exit()

        #movimentação no retângulo no teclado.                         
    
        if event.type==KEYDOWN:
            print('key')
            if event.key==K_a:
                print('a')
                if x_controle==velocidade:
                    pass
                else:
                    x_controle=-velocidade
                    y_controle=0
            if event.key==K_d:
                print('d')
                if x_controle==-velocidade:
                    pass
                else:
                    print('d')
                    x_controle=velocidade
                    y_controle=0
            if event.key==K_w:
                print('w')
                if y_controle==velocidade:
                    pass               
                else:
                    y_controle=-velocidade
                    x_controle=0
            if event.key==K_s:
                print('s')
                if y_controle==-velocidade:
                    pass         
                else:
                    y_controle=+velocidade
                    x_controle=0
           
    x_cobra=x_cobra+x_controle
    y_cobra=y_cobra+y_controle 
   
    #desenho das formas geométricas na tela      
    cobra=pygame.draw.rect(tela, (0,100,0), (x_cobra,y_cobra,13,13))
     
    maca=pygame.draw.circle(tela,(255,0,0), (x_maca,y_maca),10)
    if cobra.colliderect(maca):
         x_maca= randint(40,600)
         y_maca= randint(50,430)
         pontos+=1
         barulho_colisao.play()
         comprimento_inicial=comprimento_inicial+1           

    lista_cabeca=[]
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
     
    lista_cobra.append(lista_cabeca) 
    
    #mensagem de game over 
    if lista_cobra.count(lista_cabeca)>1:
        fonte2=pygame.font.SysFont('arial',20,True,False)
        mensagem=("Game over! pressione á tleca R para Jogar novamente")
        texto_formatado2=fonte2.render(mensagem,True,(0,0,0))        
        ret_texto=texto_formatado2.get_rect()
     
        over=True
        while over:
            tela.fill((255,50,100))
            for event in pygame.event.get():
                 if event.type==QUIT:
                     pygame.quit()
                     exit()
                 if event.type==KEYDOWN:
                     if event.key==K_r:
                         reiniciar_jogo()  
            ret_texto.center=(largura_tela//2,altura_tela//2)            
            tela.blit(texto_formatado2,ret_texto) 
            pygame.display.update()
    
    if x_cobra>largura_tela:
         x_cobra=0
    if x_cobra<0:
         x_cobra=largura_tela
    if y_cobra<0:
         y_cobra=altura_tela
    if y_cobra>altura_tela:
         y_cobra=0 
                       
    if len(lista_cobra)>comprimento_inicial:
         del lista_cobra[0] 
         
    aumenta_cobra(lista_cobra)
     
    tela.blit(texto_formato,(450,40)) 
                                   
    pygame.display.update()