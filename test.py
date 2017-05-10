#Utilities

from qtido import *
from math import cos
from math import sin


#Fonctions

def positioncalc(dt, speed, acceleration, position, M_hubble, window,time):    #On fait un pas de dt
    
    G = (6.67)*(10**(-11)) #N.m²/kg²
    M_earth = (5.9736)*(10**(24)) #kg
    if M_hubble <= 109000 : #kg
        M_hubble = 109000   #kg
        dM_hubble = 0       #kg/s
    else :
        M_hubble = M_hubble - 3654*dt #kg
        dM_hubble = 0              #kg/s
    
    altitude = (position[0]**2 + position[1]**2)**0.5 #m
    
    acceleration[0] = -G * (M_earth / (altitude**2)) * (position[0] / (altitude)) + dM_hubble * (speed[0] / M_hubble)  #Calcul de l'accélération     #m/s²
    acceleration[1] = -G * (M_earth / (altitude**2)) * (position[1] / (altitude)) + dM_hubble * (speed[1] / M_hubble)

    speed[0] += acceleration[0] * dt  #Calcul de la vitesse #m/s
    speed[1] += acceleration[1] * dt

    position[0] += speed[0] * dt  #Calcul de la position #m
    position[1] += speed[1] * dt

    draw(window,position,acceleration,speed,M_hubble, time)

    MHubble_Time = [M_hubble, time + dt]

    return MHubble_Time

def draw(window, position,acceleration,speed,M_hubble,time):

    epaisseur_du_trait(window,1)
    
    effacer(window)
    couleur(window,0,0,1)
    disque(window,475,475,399) #La Terre en Bleu
    couleur(window,1,0,0)
    cercle(window,475,475,436) #L'orbite qu'on veut en rouge
    couleur(window,0,1,0)
    disque(window,position[0]/16000 + 475,position[1]/16000 + 475,10) #Le sattelite en vert

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
    texte(window,1010,440,18,str((((position[0]**2 + position[1]**2)**(0.5)-6378000)/1000)))
    couleur(window,0,0,0)
    rectangle(window,1095,440,1150,422)
    couleur(window,1,1,1)
    texte(window,1100,440,18,'km')

    texte(window,955,500,20,'Time elapsed :') #Durée du vol
    texte(window,1010,540,18,str(time))
    couleur(window,0,0,0)
    rectangle(window,1095,540,1150,522)
    couleur(window,1,1,1)
    texte(window,1100,540,18,'s')

    if (((position[0]**2 + position[1]**2)**(0.5)-6378000)/1000) <= 0:
        couleur(window,1,0,0)
        texte(window,120,475,25,'CRASHED YOU NOOB LEARN HOW TO DRIVE')
        attendre_pendant(window,3000)

    #Cadre télémétrie
    epaisseur_du_trait(window,5)
    couleur(window,1,0.54,0.16)
    ligne(window,950,0,950,950)
    texte(window,1000,50,25,'Hubble')
    ligne(window,950,75,1150,75)
    ligne(window,950,175,1150,175)
    ligne(window,950,275,1150,275)
    ligne(window,950,375,1150,375)
    ligne(window,950,475,1150,475)

    #Fin de l'affichage télémétrie


#Main

def main():
    
#On initialise les variables
    M_hubble = 2046000     ## kg                                                                                                                                      
    window = creer(1150,950) #1px = 16km    
    position = [6390000, 0] #On commence à l'équateur #m
    speed = [200,-5300] #m/s VALEUR TROUVEE EMPIRIQUEMENT
    acceleration = [0,0] #m/s²
    time = 0 #s
    MHubble_Time = []

    while(not est_fermee(window)):
        MHubble_Time =  positioncalc(10, speed, acceleration, position, M_hubble, window, time) #On calcule les nouvelles valeurs
        M_hubble = MHubble_Time[0]
        time = MHubble_Time[1]
        attendre_pendant(window,10)

#Appel de la fonction main

main()
