Au début il faut créer les confettis. alors dans le init, il faut associer :
    la position : un random entre (-200,WIDTH) pour (x,y)
    la vitesse : entre 1 et 10
    la taille : un random entre (7, 12) pour créer une différence entre les confettis et pour que ca semble plus réel
    la couleur : les couleurs en programmation RGB, il faut trois randoms entre 0 et 255 pour avoir toutes les couleurs 

En suite, après avoir créé un confetti, il faut qu'il soit mis à jour à chaque instant. C'est ce que fait la fonction mettre_à_jour
    la nouvelle position y reçoit la vitesse de y
    la nouvelle position x reçoit la vitesse de x
    et si la position y dépasse le height:
        Créer un nouveau confetti dans une position random entre -200 et height pour les deux paramètres de position (x,y)

La fonction dessiner permet de dessiner le confetti sur le screen grâce à la fonction prédéfinie de pygame " pygame.draw.rect() "

Dans le main, j'ai créé une liste de confettis " confetti_list = [Confetti() for _ in range(100)] "
    et dans le code princiaple, quand il y a un gagnant, on parcoure la liste des confettis et on applique à chaque élement la fonction mettre_à_jour() et dessiner().