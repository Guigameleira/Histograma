import pygame, sys
from pygame.locals import QUIT
pygame.init()
tela = pygame.display.set_mode((800, 600))
import random
cor = (255,255,255)
palavra = ['sala', 'chão', 'sol', 'casa', 'time', 'hora', 'amor', 'maçã', 'luz']
listafaixas = [0,0,0,0,0,0,0,0,0]

for g in range(40):
  r = random.choice(palavra)
  if r =='sala':
    listafaixas[0] += 1
  elif r == 'casa':
    listafaixas[1] += 1
  elif r == 'chão':
    listafaixas[2] += 1
  elif r == 'sol':
    listafaixas[3] += 1
  elif r == 'luz':
    listafaixas[4] += 1
  elif r == 'time':
    listafaixas[5] += 1
  elif r == 'hora':
    listafaixas[6] += 1
  elif r == 'amor':
    listafaixas[7] += 1
  elif r == 'maçã':
    listafaixas[8] += 1
 
def desenho():
  global x0,x1,x2,x3,x4,x5,x6,x7,x8
  fonte = pygame.font.Font(pygame.font.get_default_font(),20)
  x0 = fonte.render('sala', False, (cor))
  x1 = fonte.render('casa', False, (cor))
  x2 = fonte.render('chão', False, (cor))
  x3 = fonte.render('sol', False, (cor))
  x4 = fonte.render('luz', False, (cor))
  x5 = fonte.render('time', False, (cor))
  x6 = fonte.render('hora', False, (cor))
  x7 = fonte.render('amor', False, (cor))
  x8 = fonte.render('maçã', False, (cor))
  
  alturaletras = 520
  pygame.draw.line(tela ,(255,255,255),(40,20), (40,500))  
  pygame.draw.line(tela ,(255,255,255),(680,500), (40,500))
  pygame.draw.rect(tela,(250,0,250),(120,500- listafaixas[1]*20 ,60,listafaixas[1]*20))
  pygame.draw.rect(tela,(250,0,0),(60,500- listafaixas[0]*20 , 60 ,listafaixas[0]*20))
  pygame.draw.rect(tela,(3, 102, 252),(180,500- listafaixas[2]*20 ,60,listafaixas[2]*20))
  pygame.draw.rect(tela,(34, 255, 0),(240,500- listafaixas[3]*20 ,60,listafaixas[3]*20))
  pygame.draw.rect(tela,(252, 244, 3),(300,500- listafaixas[4]*20 ,60,listafaixas[4]*20))
  pygame.draw.rect(tela,(255, 77, 0),(360,500- listafaixas[5]*20 ,60,listafaixas[5]*20))
  pygame.draw.rect(tela,(0, 255, 128),(420,500- listafaixas[6]*20 ,60,listafaixas[6]*20))
  pygame.draw.rect(tela,(132, 255, 0),(480,500- listafaixas[7]*20 ,60,listafaixas[7]*20))
  pygame.draw.rect(tela,(255, 3, 104),(540,500- listafaixas[8]*20 ,60,listafaixas[8]*20))
   
  tela.blit(x0,x0.get_rect(top = alturaletras , left = 55))
  tela.blit(x1,x1.get_rect(top = alturaletras , left = 115))
  tela.blit(x2,x2.get_rect(top = alturaletras , left = 175))
  tela.blit(x3,x3.get_rect(top = alturaletras , left = 245))
  tela.blit(x4,x4.get_rect(top = alturaletras , left = 305))
  tela.blit(x5,x5.get_rect(top = alturaletras , left = 365))
  tela.blit(x6,x6.get_rect(top = alturaletras , left = 425))
  tela.blit(x7,x7.get_rect(top = alturaletras , left = 485))
  tela.blit(x8,x8.get_rect(top = alturaletras , left = 545))
  
def linhas():
  pygame.draw.line(tela ,(255,255,255),(40,400), (30,400))  
  pygame.draw.line(tela ,(255,255,255),(40,350), (30,350))  
  pygame.draw.line(tela ,(255,255,255),(40,300), (30,300))  
  pygame.draw.line(tela ,(255,255,255),(40,250), (30,250))  
  pygame.draw.line(tela ,(255,255,255),(40,200), (30,200))  
  pygame.draw.line(tela ,(255,255,255),(40,150), (30,150))  
  pygame.draw.line(tela ,(255,255,255),(40,100), (30,100))
  pygame.draw.line(tela ,(255,255,255),(40,50), (30,50))
  pygame.draw.line(tela ,(255,255,255),(40,0), (30,0))
  pygame.draw.line(tela ,(255,255,255),(40,100), (30,100))
 
desenho()
linhas()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    tela.fill(0)
    desenho()
    linhas()
    pygame.display.update()
