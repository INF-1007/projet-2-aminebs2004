import numpy as np
import pygame
from specifications import DENSITE_AIR

class Vehicule:
    # TODO : Créer le constructeur 
    #def __init__(self,nom,position_dep,roues,moteur,Specs,chassis,image_path):
    def __init__(self,nom,position_dep,roues,moteur,chassis,Specs,image):
        self.__nom = nom
        self.__position= np.array(position_dep, dtype=float)
        self.__vitesse = np.array([0.0,0.0])
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__Specs = Specs
        self.__poids_total = self.calculer_poids_total()
        # TODO : ajouter un attribut pour l'image du véhicule

        self.image = pygame.transform.scale(pygame.image.load(image), (self.__Specs.image_width , self.__Specs.image_height))
    
    @property
    def position(self):
        return self.__position
    
    def affichage_vehicule(self, screen):
        screen.blit(self.image, (int(self.__position[0]-self.__Specs.image_width), int(self.__position[1])))
    
    def calculer_poids_total(self):
        return (len(self.__roues) * self.__Specs.roue_poids + self.__Specs.chassis_poids + self.__Specs.moteur_poids)
        
    def calculer_traction(self):
        return (self.calculer_poids_total() * self.__Specs.moteur_acceleration)

    def calculer_trainee(self):
        return (1/2 * self.__Specs.chassis_trainee * self.__Specs.chassis_aire * DENSITE_AIR * self.__vitesse ** 2)

    def calculer_friction(self):
        return (self.__Specs.roue_friction * self.__vitesse)

    def accelerer(self, dt):
        acceleration = (self.calculer_traction() - self.calculer_trainee() - self.calculer_friction()) / self.calculer_poids_total()
        self.__vitesse += int(list(acceleration)[0]) * dt
        self.__position[0] += int((list(self.__vitesse))[0]) * dt

    def celebrer(self):
        return f"{self.__nom} remporte la course !"