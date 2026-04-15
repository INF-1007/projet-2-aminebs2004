import pygame
from moto import Moto
from auto import Auto
from camion import Camion
from confettis import Confetti
from config import WIDTH, HEIGHT, START_LINE_X, FINISH_LINE_X, START_MOTO_Y, START_AUTO_Y, START_CAMION_Y 

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation de course")

    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # TODO : Créer une liste de véhicules qui contient une instance pour chaque
    # type de véhicule : une moto, une auto et un camion
    vehicules = [Moto('Moto',[START_LINE_X,START_MOTO_Y],'images/moto.png'),
                 Auto('Auto',[START_LINE_X,START_AUTO_Y],'images/auto.png'),
                 Camion('Camion',[START_LINE_X,START_CAMION_Y],'images/camion.png')]



    running = True
    course_commencee = False
    gagnant = None
    confetti_list = [Confetti() for _ in range(100)]
    while running:

        screen.blit(background, (0, 0))

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    course_commencee = True
        for veh in vehicules:
            if course_commencee:
                veh.accelerer(dt)
            if veh.position[0] >= FINISH_LINE_X and gagnant is None:
                gagnant = veh
        for veh in vehicules:
            veh.affichage_vehicule(screen)


        # TODO : Gérer le début de la course en appelant la méthode `accelerer` des véhicules
        # Si le véhicule franchit la ligne et qu’on n’a pas encore de gagnant, on le note


        # TODO : Pour chaque véhicule, appeler la méthode `affichage_vehicule`
        

        if not course_commencee and gagnant is None:
            txt = font.render("Appuyez sur ESPACE pour démarrer",
                              True, (0, 0, 0))
            screen.blit(txt, (350, 35))

        # TODO: Si on a un gagnant, afficher le message qui indique le véhicule gagnant avec la méthode `celebrer` 
        
        if gagnant:
            txt = font.render(gagnant.celebrer(), True, (0, 0, 0))
            screen.blit(txt, (350, 35))
            for c in confetti_list:
                c.mettre_à_jour()
                c.dessiner(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()