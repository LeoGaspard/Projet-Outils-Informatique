#Utilities

from qtido import *
from math import cos
from math import sin


#Fonctions

def positioncalc(dt, speed, acceleration, position, M_hubble, window):    #On fait un pas de dt
    
    G = (6.67)*(10**(-14))
    M_earth = (5.9736)*(10**(24))
    if M_hubble <= 109000 :
        M_hubble = 109000
        dM_hubble = 0
    else :
        M_hubble = M_hubble - 3654*dt
        dM_hubble = 3654
    
    altitude = (position[0]**2 + position[1]**2)**0.5
    
    acceleration[0] = -G * (M_earth / (altitude**2)) * (position[0] / (altitude)) - dM_hubble * (speed[0] / M_hubble)  #Calcul de l'accélération
    acceleration[1] = -G * (M_earth / (altitude**2)) * (position[1] / (altitude)) - dM_hubble * (speed[1] / M_hubble)

    speed[0] += acceleration[0] * dt #Calcul de la vitesse
    speed[1] += acceleration[1] * dt

    position[0] += speed[0] * dt #Calcul de la position
    position[1] += speed[1] * dt

    draw(window,position,acceleration,speed,M_hubble)

    return M_hubble

def draw(window, position,acceleration,speed,M_hubble):

    epaisseur_du_trait(window,1)
    
    effacer(window)
    couleur(window,0,0,1)
    disque(window,475,475,399) #La Terre en Bleu
    couleur(window,1,0,0)
    cercle(window,475,475,436) #L'orbite qu'on veut en rouge
    couleur(window,0,1,0)
    disque(window,position[0]/16 + 475,position[1]/16 + 475,10) #Le sattelite en vert

    couleur(window,1,1,1)

    #Affichage de la télémétrie
    couleur(window,0,0,0)
    rectangle(window,950,0,1150,950)

    couleur(window,1,1,1)
    texte(window,955,100,20,'Speed :') #La vitesse
    texte(window,1010,140,18,str((speed[0]**2 + speed[1]**2)**(0.5)))
    couleur(window,0,0,0)
    rectangle(window,1095,140,1150,122)
    couleur(window,1,1,1)
    texte(window,1100,140,18,'m/s')

    texte(window,955,200,20,'Acceleration :') #L'accélération
    texte(window,1010,240,18,str((acceleration[0]**2 + acceleration[1]**2)**(0.5)))
    couleur(window,0,0,0)
    rectangle(window,1095,240,1150,222)
    couleur(window,1,1,1)
    texte(window,1100,240,18,'m/s²')

    texte(window,955,300,20,'Weight :') #Le poids
    texte(window,1010,340,18,str(M_hubble))
    couleur(window,0,0,0)
    rectangle(window,1100,340,1150,322)
    couleur(window,1,1,1)
    texte(window,1100,340,18,'kg')

    texte(window,955,400,20,'Altitude :') #L'altitude
    texte(window,1010,440,18,str((position[0]**2 + position[1]**2)**(0.5)-6378))
    couleur(window,0,0,0)
    rectangle(window,1095,440,1150,422)
    couleur(window,1,1,1)
    texte(window,1100,440,18,'m')

    #Cadre télémétrie
    epaisseur_du_trait(window,5)
    couleur(window,1,0.54,0.16)
    ligne(window,950,0,950,950)
    texte(window,1000,50,25,'Hubble')
    ligne(window,950,75,1150,75)
    ligne(window,950,175,1150,175)
    ligne(window,950,275,1150,275)
    ligne(window,950,375,1150,375)

    #Fin de l'affichage télémétrie


#Main

def main():
    
#On initialise les variables
    M_hubble = 2046000                                                                                                                                            
    window = creer(1150,950) #1px = 16km    
    position = [6378, 0] #On commence à l'équateur
    speed = [-400,-8500]
    acceleration = [0,0]
    attendre_pendant(window,1000)

    while(not est_fermee(window)):
        M_hubble =  positioncalc(0.01, speed, acceleration, position, M_hubble, window) #On calcule les nouvelles valeurs
        attendre_pendant(window,10)

#Appel de la fonction main

main()
