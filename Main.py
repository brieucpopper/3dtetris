#IMPORTS
from numba import jit
import numpy as np
import time, pygame
import random
from FonctionsAux import *
from Database import *


pygame.init()


pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
pygame.mouse.set_pos = (420, 69)
compteur = 0

screen = pygame.display.set_mode((width,height))


score = 0
game_over = False
pygame.font.init()
surface = pygame.Surface((width, height))
police = pygame.font.SysFont("Helvetica",10)

objet_actif[0]=np.array([dim3-4,dim2-2,5])
objet_actif[1]=np.array(objets[random.randint(0,len(objets)-1)])
objet_actif[2]=random.randint(1,len(couleurs)-1)

while not game_over:
    
    if compteur == int((10-8*(score/(200+score)))):
        print(joueur)
        compteur = 0        
        if not(objet(objet_actif[0],objet_actif[0]+np.array([0,-1,0]),objet_actif[1],objet_actif[1],objet_actif[2])):
            
            if objet_actif[0][1] == dim2-2:
                game_over = True
            else:
                score = verif_lignes(score)
                print("nouveau\n"*10)
                objet_actif[0]=np.array([dim3-4,dim2-2,5])
                objet_actif[1]=np.array(objets[random.randint(0,len(objets)-1)])
                objet_actif[2]=random.randint(1,len(couleurs)-1)
    else:
        compteur+=1
            
    temps1=time.time()
    souris = pygame.mouse.get_rel()
    matrice_regard = rotation_haut_bas(matrice_regard,-souris[1]/1000)
    matrice_regard = rotation_dgregard(matrice_regard,souris[0]/1000)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            depl=np.array([0,0,0])
            if event.key == pygame.K_w:#avancer
                depl=np.array(matrice_regard[0])
                
            if event.key == pygame.K_s:#reculer
                depl=np.array(-matrice_regard[0])
                
            if event.key == pygame.K_SPACE:#monter
                depl=np.array(-matrice_regard[1])
                
            if event.key == pygame.K_a:#gauche
                depl=np.array(-matrice_regard[2])
                
            if event.key == pygame.K_d:#droite
                depl=np.array(matrice_regard[2])
                
            if event.key == pygame.K_LSHIFT:#descendre
                depl=np.array(matrice_regard[1])

            joueur=joueur+depl
            
            
            

            if event.key == pygame.K_ESCAPE:
                game_over=True
                
            #DEPLACEMENT DES BLOCS
            inc=np.array([0,0,0],dtype="int")
            if event.key == pygame.K_LEFT:
                inc=np.array([0,0,1])


                
            if event.key == pygame.K_RIGHT:
                inc=np.array([0,0,-1])

            
            if event.key == pygame.K_y:
                if score>100:
                    objet(objet_actif[0],objet_actif[0],objet_actif[1],rotationner(3,objet_actif[1]),objet_actif[2])
                    score-=100

                
            if event.key == pygame.K_DOWN:
                if not(objet(objet_actif[0],objet_actif[0]+np.array([0,-1,0]),objet_actif[1],objet_actif[1],objet_actif[2])):
                    #CHECK LIGNE PLEINE
                    print("nouveau\n"*10)
                    score = verif_lignes(score)
                    objet_actif[0]=np.array([dim3-4,dim2-2,5])
                    objet_actif[1]=np.array(objets[random.randint(0,len(objets)-1)])
                    objet_actif[2]=random.randint(1,len(couleurs)-1)






                
            objet(objet_actif[0],objet_actif[0]+inc,objet_actif[1],objet_actif[1],objet_actif[2])
                
        if event.type == pygame.MOUSEBUTTONDOWN:
                
                if(event.button==1):
                    objet(objet_actif[0],objet_actif[0],objet_actif[1],rotationner(1,objet_actif[1]),objet_actif[2])
                elif(event.button==3):
                    objet(objet_actif[0],objet_actif[0],objet_actif[1],rotationner(2,objet_actif[1]),objet_actif[2])
    matriceprojj = np.zeros((width,height,3))
    for i in range(dim1):
        for j in range(dim2):
            for k in range(dim3):

                e = espace[i][j][k]
                if e != 0:
                    coin4=rayon(np.array([i+1,j,k]),e,joueur,matrice_regard)
                    coin3=rayon(np.array([i,j+1,k]),e,joueur,matrice_regard)
                    coin2=rayon(np.array([i,j,k+1]),e,joueur,matrice_regard)
                    coin1=rayon(np.array([i,j,k]),e,joueur,matrice_regard)
                    coin5=rayon(np.array([i+1,j+1,k]),e,joueur,matrice_regard)
                    coin6=rayon(np.array([i+1,j,k+1]),e,joueur,matrice_regard)
                    coin7=rayon(np.array([i,j+1,k+1]),e,joueur,matrice_regard)
                    coin8=rayon(np.array([i+1,j+1,k+1]),e,joueur,matrice_regard)
                    matriceprojj=line(coin1,coin2,matriceprojj)
                    matriceprojj=line(coin1,coin4,matriceprojj)
                    matriceprojj=line(coin1,coin3,matriceprojj)
                    matriceprojj=line(coin4,coin5,matriceprojj)
                    matriceprojj=line(coin8,coin7,matriceprojj)
                    matriceprojj=line(coin8,coin6,matriceprojj)
                    matriceprojj=line(coin8,coin5,matriceprojj)
                    matriceprojj=line(coin2,coin6,matriceprojj)
                    matriceprojj=line(coin2,coin7,matriceprojj)
                    matriceprojj=line(coin3,coin7,matriceprojj)
                    matriceprojj=line(coin3,coin5,matriceprojj)
                    matriceprojj=line(coin4,coin6,matriceprojj)
                    # THANK YOU BRIOUQUE

    surface = pygame.pixelcopy.make_surface(matriceprojj.astype(int))
    
    texte = "Score : " + str(score) + " ,press y for 3eme dimension coute 100 pts"
    textsurface = police.render(texte, False, (255, 255, 255))
    
    screen.blit(surface, [0,0])
    screen.blit(textsurface,[0,0])
    pygame.display.flip()
    
    temps2=time.time()
    print(temps2-temps1)
    if temps2-temps1>0.07:
        print("t'as cassé la matrice")
    else:
        time.sleep(0.07-(temps2-temps1))

time.sleep(3)
pygame.quit()























