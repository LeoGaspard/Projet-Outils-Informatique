#Utilities

from qtido import *
from math import cos
from math import sin


#Fonctions

def positioncalc(dt, speed, acceleration, position, M_hubble):    #On fait un pas de dt
    G = (6.67)*(10**(-14))
    M_earth = (5.9736)*(10**(24))
    if M_hubble <= 109000 :
        M_hubble = 109000
        dM_hubble = 0
    else :
        M_hubble = M_hubble - 3654*dt
        dM_hubble = 3654
    
    altitude = (position[0]**2 + position[1]**2)**0.5
    
    acceleration[0] = -G * (M_earth / (altitude**2)) * (position[0] / (altitude)) - dM_hubble * (speed[0] / M_hubble) #Calcul de l'accélération
    acceleration[1] = -G * (M_earth / (altitude**2)) * (position[1] / (altitude)) - dM_hubble * (speed[1] / M_hubble)

    speed[0] += acceleration[0] * dt #Calcul de la vitesse
    speed[1] += acceleration[1] * dt

    position[0] += speed[0] * dt #Calcul de la position
    position[1] += speed[1] * dt


def draw(window, position):
    
    effacer(window)
    couleur(window,0,0,1)
    disque(window,475,475,399) #La Terre en Bleu
    couleur(window,1,0,0)
    cercle(window,475,475,436) #L'orbite qu'on veut en rouge
    couleur(window,0,1,0)
    disque(window,position[0]/16 + 475,position[1]/16 + 475,10) #Le sattelite


#Main

def main():
    
#On initialise les variables
    M_hubble = 2046000                                                                                                                                            
    window = creer(950,950) #1px = 16km    
    position = [6378, 0] #On commence à l'équateur
    speed = [14,12]
    acceleration = [0,0]

    draw(window, position)
    attendre_pendant(window,1000)

    while(not est_fermee(window)):
        positioncalc(1, speed, acceleration, position, M_hubble) #On calcule les nouvelles valeurs
        draw(window, position)
        attendre_pendant(window,1000)
        print('Position :', position, '\n Vitesse', speed, '\n Acceleration', acceleration, '\n -----------------')

#Appel de la fonction main

main()
