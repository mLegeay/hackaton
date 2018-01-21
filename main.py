from analyse_flechette import FlechetteSciKit, TreshAnalyse, FlechetteScene, Polygone

# Retirer le commentaire pour pouvoir utiliser les requêtes HTTP avec Python
# pip install requests
# from requests import get, post

# Couleur Rouge = x3
# Couleur Vert = x2
# Couleur Noir = x1
# Couleur Centre Rouge = 50 pts
# Couleur Centre Vert = 25 pts


POLYGONES_SECTEURS = [
    # Secteur n°1
    Polygone(
        [
            (515, 154),
            (590, 190),
            (570, 250),
            (550, 330),
            (520, 390),
            (520, 320),
            (517, 220)
        ]
    ),
    # Secteur n°2
    Polygone(
        [
            (650, 650),
            (620, 600),
            (570, 512),
            (540, 440),
            (588, 500),
            (658, 580),
            (697, 632)
        ]
    ),
    # Secteur n° ...
]

FRM_ANALYSE_TARGET = 50  # Numéro de la FRM à analyser, la valeur 50 est arbitraire !
FRM_ANALYSE_DROITE_HAUT_ACTIF = True  # Toggle pour forcer l'analyse / découverte des flechettes sur la vue haute et droite. !Attention! CPU Utilisation Élevée

if __name__ == '__main__':

    # On récupère l'ensemble des sessions de jeu disponible (arbo. fichiers mp4)
    scenes_disponibles = FlechetteScene.get_scenes()

    for scene in scenes_disponibles:

        print('Analyse vidéo de FACE "{0}"'.format(scene.face))

        analyse_scene = FlechetteSciKit(scene.face)

        if FRM_ANALYSE_DROITE_HAUT_ACTIF:
            analyse_scene_droite = FlechetteSciKit(scene.droite)
            analyse_scene_haut = FlechetteSciKit(scene.haut)

        tresh = analyse_scene.diff_n(FRM_ANALYSE_TARGET, False)

        if FRM_ANALYSE_DROITE_HAUT_ACTIF:
            tresh_droite = analyse_scene_droite.diff_n(FRM_ANALYSE_TARGET, False)
            tresh_haut = analyse_scene_haut.diff_n(FRM_ANALYSE_TARGET, False)

        print('Coeff SSIM FRM 0-50: {0}'.format(analyse_scene.coeff_ssim_n(FRM_ANALYSE_TARGET)))

        # On récupère les flechettes présentes sur l'image
        flechettes = TreshAnalyse.get_flechettes(tresh, debug=False)

        flechettes_droite = TreshAnalyse.get_flechettes(tresh_droite, debug=False)
        flechettes_haut = TreshAnalyse.get_flechettes(tresh_haut, debug=False)

        # Affichage du nombre de flechette en fonction de la vue
        print('Nombre flechette(s) FACE FRM 50: {0}'.format(len(flechettes)))

        if FRM_ANALYSE_DROITE_HAUT_ACTIF:
            print('Nombre flechette(s) DROITE FRM 50: {0}'.format(len(flechettes_droite)))
            print('Nombre flechette(s) HAUT FRM 50: {0}'.format(len(flechettes_haut)))

        # On effectue un traitement pour chaque flechette découverte sur la FRM n° 50
        for flechette, i in zip(flechettes, range(len(flechettes))):

            # On essaie de découvrir la couleur touchée par la flechette
            couleur_flechette_tete_guess = analyse_scene.get_color_name_guess(flechette.x + flechette.width,
                                                                              flechette.y)

            print('#{0} {1} -- COLOR_GUESS {2}'.format(i, str(flechette), couleur_flechette_tete_guess))

            # On vérifie si la flechette ne serai pas présente dans un des polygones définis en constante, cf. en-têtes
            # Équivaut à POUR CHAQUE polygone FAIRE ... FIN
            for secteur_polygone, secteur_id in zip(POLYGONES_SECTEURS, range(1, len(POLYGONES_SECTEURS) + 1)):

                # On vérifie si la coordonnée est dans le polygone courant du POUR CHAQUE
                if secteur_polygone.inside_polygon(flechette.x + flechette.width, flechette.y) is True:

                    print('La flechette est dans le secteur {0} ! '.format(secteur_id))

                    # Votre logique pour le score
                    if couleur_flechette_tete_guess == 'BLACK':
                        pass
                    if couleur_flechette_tete_guess == 'RED':
                        pass
                    if couleur_flechette_tete_guess == 'GREEN':
                        pass
                    if couleur_flechette_tete_guess == 'WHITE':
                        pass

                    # Utilisez la fonction get ou post pour transmettre votre résultat à un serveur distant..

        print()

    exit()

    kk = FlechetteSciKit('VIDEO-SRC/CAM-FACE/20180120-10h26-1516440391.mp4')

    # Affiche les meta de fichier vidéo
    print("Affiche les meta de fichier vidéo")
    print(kk.meta)

    # Affiche le nombre d'image présente dans la vidéo
    print("Affiche le nombre d'image présente dans la vidéo")
    print(kk.nframes)

    # Affiche le coeff de différence entre image 1 et image 50
    print("Affiche le coeff de différence entre image 1 et image 50")
    print(kk.coeff_ssim_n(50))

    # Affiche les coord des cases ROUGES
    print("Affiche les coord des cases ROUGES")
    print(kk.get_cases_rouges())

    # kk.cases_rouges_plot()

    # Affiche les différences notables entre l'image 1 et image 50
    print("Affiche les différences notables entre l'image 1 et image 50")
    tresh = kk.diff_n(50, False)

    # print(type(tresh))
    # print(tresh.tolist())

    # On récupère les flechettes présentes sur l'image
    flechettes = TreshAnalyse.get_flechettes(tresh, debug=True)

    for flechette, i in zip(flechettes, range(len(flechettes))):
        print('#{0} {1}'.format(i, str(flechette)))

    # Maintenant, vous pouvez trouver la tête de la flechette sachant l'orientation de la caméra.

    # Le résultat tresh est au format numpy.ndarray
    # mathieu.legeay72360@gmail.com

    exit()

    # for num in nums:
    #
    #     image = vid.get_data(num)
    #     fig = pylab.figure()
    #     fig.suptitle('image #{}'.format(num), fontsize=20)
    #     pylab.imshow(image)
    #
    # pylab.show()
