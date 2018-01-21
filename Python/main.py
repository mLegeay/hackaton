from analyse_flechette import FlechetteSciKit, TreshAnalyse, FlechetteScene, Polygone
import json

# Retirer le commentaire pour pouvoir utiliser les requêtes HTTP avec Python
# pip install requests
# from requests import get, post

# Couleur Rouge = x3
# Couleur Vert = x2
# Couleur Noir = x1
# Couleur Centre Rouge = 50 pts
# Couleur Centre Vert = 25 pts


POLYGONES_SECTEURS = [
        {
            'point': 1,
            'polygone': Polygone(
                [
                    (516, 157),
                    (584, 190),
                    (526, 393),
                ]
            )
        },
        {
            'point': 2,
            'polygone': Polygone(
                [
                    (698, 632),
                    (648, 650),
                    (539, 440),
                ]
            )
        },
        {
            'point': 3,
            'polygone': Polygone(
                [
                    (589, 632),
                    (536, 610),
                    (529, 442),
                ]
            )
        },
        {
            'point': 4,
            'polygone': Polygone(
                [
                    (712, 340),
                    (655, 255),
                    (537, 406),
                ]
            )
        },
        {
            'point': 5,
            'polygone': Polygone(
                [
                    (452, 151),
                    (403,174),
                    (513, 390),
                ]
            )
        },
        {
            'point': 6,
            'polygone': Polygone(
                [
                    (752, 520),
                    (748, 438),
                    (545, 423),
                ]
            )
        },
        {
            'point': 7,
            'polygone': Polygone(
                [
                    (483, 581),
                    (436, 531),
                    (515, 434),
                ]
            )
        },
        {
            'point': 8,
            'polygone': Polygone(
                [
                    (369, 404),
                    (396, 468),
                    (506, 419),
                ]
            )
        },
        {
            'point': 9,
            'polygone': Polygone(
                [
                    (369, 219),
                    (354, 271),
                    (506, 396),
                ]
            )
        },
        {
            'point': 10,
            'polygone': Polygone(
                [
                    (735, 589),
                    (754, 524),
                    (544, 430),
                ]
            )
        },
        {
            'point': 11,
            'polygone': Polygone(
                [
                    (368, 401),
                    (352, 336),
                    (504, 410),
                ]
            )
        },
        {
            'point': 12,
            'polygone': Polygone(
                [
                    (369, 214),
                    (402, 175),
                    (508, 393),
                ]
            )
        },
        {
            'point': 13,
            'polygone': Polygone(
                [
                    (746, 434),
                    (713, 344),
                    (542, 414),
                ]
            )
        },
        {
            'point': 14,
            'polygone': Polygone(
                [
                    (354, 273),
                    (353, 333),
                    (504, 403),
                ]
            )
        },
        {
            'point': 15,
            'polygone': Polygone(
                [
                    (698, 631),
                    (734, 590),
                    (543, 437),
                ]
            )
        },
        {
            'point': 16,
            'polygone': Polygone(
                [
                    (396, 469),
                    (434, 529),
                    (509, 428),
                ]
            )
        },
        {
            'point': 17,
            'polygone': Polygone(
                [
                    (594, 645),
                    (647, 650),
                    (534, 442),
                ]
            )
        },
        {
            'point': 18,
            'polygone': Polygone(
                [
                    (653, 254),
                    (596, 192),
                    (531, 398),
                ]
            )
        },
        {
            'point': 19,
            'polygone': Polygone(
                [
                    (483, 581),
                    (535, 619),
                    (521, 440),
                ]
            )
        },
        {
            'point': 20,
            'polygone': Polygone(
                [
                    (513, 155),
                    (454, 150),
                    (518,390),
                ]
            )
        },
    # polygones +={
     #       'point': 25,
       #     'polygone': polygone([526, 393], [539, 440], [529, 442], [537,406], [513, 390], [545, 423], [515, 434], [506, 419], [544, 430])
      #  }
]

FRM_ANALYSE_TARGET = 30  # Numéro de la FRM à analyser, la valeur 50 est arbitraire !
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

        listhit = []
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
                if secteur_polygone['polygone'].inside_polygon(flechette.x + flechette.width, flechette.y) is True:

                    print('La flechette est dans le secteur {0} ! '.format(secteur_id))
                    hit = {'case':secteur_id, 'couleur':couleur_flechette_tete_guess}
                    print(hit)
                    listhit.append(hit)
                    print(listhit)
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

        with open('data.txt', 'w') as outfile:
            json.dump(listhit, outfile)

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
