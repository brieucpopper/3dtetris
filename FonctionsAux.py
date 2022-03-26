
#produit vectoriel np.cross(a,b)
import numpy as np
import random
#numpy.linalg.norm(a-b)
from numba import jit
from Database import *


def scal(a,b):
    return (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])


def rotation_dg(mat, teta):
    matrice = np.array([[np.cos(teta),0,np.sin(teta)],[0, 1, 0],[-np.sin(teta),0,np.cos(teta)]])
   
    return np.dot(matrice,mat)


def rotation_haut_bas(mat, teta):
    
    matrice = np.array([[np.cos(teta),-np.sin(teta),0],[np.sin(teta),np.cos(teta),0],[0,0,1]])
    #print("gloug",mat,"\n\n\n\n\n\n\n\n\n\n\n",matrice)
    return np.dot(matrice,mat)


def rotation_3(mat, teta):
    matrice = np.array([[1,0,0],[0,np.cos(teta),-np.sin(teta)],[0,np.sin(teta),np.cos(teta)]])


   
    return np.dot(matrice.astype(int),mat.astype(int))


def rotation_dgregard(mat, teta):
    x = np.arccos(min(np.sqrt((scal(mat[0],[1,0,0]))**2 + (scal(mat[0],[0,0,-1]))**2),1))
    if scal(mat[0],[0,1,0])<=0:
            x = -x
    poubelle = rotation_haut_bas(mat,-x)
    mat_poubelle = rotation_dg(poubelle, teta)
    return rotation_haut_bas(mat_poubelle,x)


def min4(a,b,c,d):
    return min(min(a,b),min(c,d))


def max4(a,b,c,d):
    return max(max(a,b),max(c,d))


@jit(nopython=True)
def pseudo_bresenham(a,b,c,d,couleur,matriceproj):
    """ Prend en entrée deux points du plan et trace une ligne entre eux en
    complétant les points qui les séparent selon la méthode de Bresenham """
    
    
    couleur=couleurs[couleur]
    def inn(a,b):
        if(0<a and a<1000 and 0<b and b<700):
            return True
        return False
    
    A = np.array([a,b])
    B = np.array([c,d])
    # Les points ont la même abscisse
    if A[0] == B[0]:
        n = B[1]-A[1]
        
        # Les points sont confondus
        if n == 0:
            if inn(A[0],A[1]):
                matriceproj[A[0]][A[1]] = couleur
            
        # B est strictement au-dessus de A
        elif n > 0:
            for i in range(n+1):
                if inn(A[0],A[1]+i):
                    matriceproj[A[0]][A[1]+i] = couleur
        
        # B est strictement en-dessous de A
        else:
            n = -n
            for i in range(n+1):
                if inn(A[0],B[1]+i):
                    matriceproj[A[0]][B[1]+i] = couleur
    
    
    
    # Les points ont la même ordonnée
    elif A[1] == B[1]:
        n = B[0]-A[0]
        
        # B est strictement à droite de A
        if n > 0:
            for i in range(n+1):
                if inn(A[0]+i,A[1]):
                    matriceproj[A[0]+i][A[1]] = couleur
        
        # B est strictement à gauche de A
        else:
            n = -n
            for i in range(n+1):
                if inn(B[0]+i,A[1]):
                    matriceproj[B[0]+i][A[1]] = couleur
    
    
    
    # Les points sont intéressants
    else:
        
        # 1er cas : le coefficient directeur est plus petit que 1
        # On trace alors en faisant augmenter x
        if abs((B[1]-A[1])/(B[0]-A[0])) <= 1:
            # B est à gauche de A -> on inverse A et B
            # (on ne se déplace que dans le sens des x croissants)
            if B[0]-A[0] < 0:
                A,B = B,A
            
            # Calculs du coefficient directeur et initialisation de x,y
            dx = B[0]-A[0]
            dy = B[1]-A[1]
            c = dy/dx
            
            if c > 0: # Indique si y doit augmenter ou descendre
                kronecher = +1
            else:
                kronecher = -1
                
            x = A[0]
            y = A[1]
            if inn(x,y):
                matriceproj[x][y] = couleur
            
            # Tracé de la ligne joignant A et B
            for i in range(dx):
                x += 1 # x augmente à chaque étape
                yreel = A[1]-c*A[0]+c*x # calcul de la valeur théorique de y
                # y augmente ou non selon sa proximité avec la valeur théorique
                if abs(yreel-y)>abs(y+kronecher*1-yreel):
                    y = y+kronecher*1
                if inn(x,y):
                    matriceproj[x][y] = couleur
        
        # 2ème cas : le coefficient directeur est plus grand que 1 :
        # les rôles de A et B sont inversés
        else:
            if B[1]-A[1] < 0:
                A,B = B,A
                
            dx = B[0]-A[0]
            dy = B[1]-A[1]
            c = dy/dx
            
            if c > 0:
                kronecher = +1
            else:
                kronecher = -1
                
            x = A[0]
            y = A[1]
            if inn(x,y):
                matriceproj[x][y] = couleur
            
            for i in range(dy):
                y += 1
                xreel = (y-A[1]+c*A[0])/c
                if abs(xreel-x)>abs(x+kronecher*1-xreel):
                    x = x+kronecher*1
                if inn(x,y):
                    matriceproj[x][y] = couleur
    return matriceproj


def rayon(coord,e,j,m): #modifier matriceproj en fonction du rayon
    v = np.add(coord,-j)
    if(np.dot(v,m[0])>0): # le point est susceptible d'etre vu(pas dans le dos ou pile sur le cote)
        #on veut coord dans la base orthonormee dregard dbas dgauche
        alpha=np.dot(v,m[0])
        beta=np.dot(v,m[1])
        gamma=np.dot(v,m[2])
        coordsurplan = np.array([beta/alpha,gamma/alpha])
        couleur=np.array([0,0,0])
        couleur=e
        
        
         #notre rayon a une projection dans le champ de vision
           #coordsuplan[0] est sur [-largeur/2;largeur/2] et on doit le mettre sur [0;699]

           #PROBLEME DISTANCE A FAIRE ICI

        return([[int(1000*coordsurplan[1]/longueur)+499,int(700*coordsurplan[0]/largeur)+349],couleur])


def line(a,b,m):
    
    if(a!=None and b !=None):
        
        
        aa=a[1]
        
        A=a[0]
        B=b[0]
    
        
        if((0<=A[0]<1000 and 0<=A[1]<700) or (0<=B[0]<1000 and 0<=B[1]<700)):#si un des deux points est a l'ecran
           
            mm=pseudo_bresenham(A[0],A[1],B[0],B[1],aa,m)
            return mm
    return m


def objet(oldcoord,coord,oldform,newforme,ggg):
    aeuautorisation=False
    if(autorisation(oldcoord,coord,oldform,newforme)):
        
        aeuautorisation=True
        objet_actif[0]=np.array(coord,dtype="int")
        objet_actif[1]=np.array(newforme,dtype="int")
        #effacage ancien
        x=oldcoord[0]
        y=oldcoord[1]
        z=oldcoord[2]

        for i in oldform:
            #i prend la valeur des coord des blocs des objets
            espace[x+i[0]][y+i[1]][z+i[2]] = 0



        #dessin nouveau

        x=coord[0]
        y=coord[1]
        z=coord[2]

        for i in newforme:
            #i prend la valeur des coord des blocs des objets
            espace[x+i[0]][y+i[1]][z+i[2]] = ggg
    return aeuautorisation


def autorisation(oldcoord, coord, oldforme, forme):
    x=oldcoord[0]
    y=oldcoord[1]
    z=oldcoord[2]

    espace_virtuel = np.copy(espace)
    
    for i in oldforme:
        
        #i prend la valeur des coord des blocs des objets
        espace_virtuel[x+i[0]][y+i[1]][z+i[2]] = 0
    
    res = True
    x=coord[0]
    y=coord[1]
    z=coord[2]

    for i in forme:
        
        if (x+i[0]<0) or (x+i[0]>dim1-1) or (y+i[1]<0) or (y+i[1]>dim2-1) or (z+i[2]<0) or (z+i[2]>dim3-1):
            res = False
        elif espace_virtuel[x+i[0]][y+i[1]][z+i[2]]!=0:
            res = False
            
        #i prend la valeur des coord des blocs des objets
    
    
    return res


def rotationner(n,f):
    print(f)
    nf=np.zeros((len(f),3),dtype='int')

    if(n==1):
        
        for i in range(len(f)):
            nf[i]=rotation_3(f[i],-np.pi/2)   
            
    if(n==2):
        
        for i in range(len(f)):
            nf[i]=rotation_3(f[i],np.pi/2)

    if(n==3):
        
        for i in range(len(f)):
            nf[i]=rotation_haut_bas(f[i],np.pi/2)
    
    print(nf)
    return(nf.astype(int))


def verif_lignes(score):
    lignes_non_pleines = []

    print("vérification")
    for i in range(1,dim2-1):
        ligne = True
        for j in range(1,dim3-1):
            if espace[-4][i][j] == 0:
                ligne = False
                break
        if not ligne:
            lignes_non_pleines.append(i)

    for i in range(len(lignes_non_pleines)):
        for j in range(1,dim3-1):
            espace[-4][i+1][j] = espace[-4][lignes_non_pleines[i]][j]

    for i in range(len(lignes_non_pleines),dim2-2):
        score += random.choice([69,42])
        for j in range(1,dim3-1):
            espace[-4][i+1][j] = 0

    return score
