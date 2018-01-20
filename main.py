from analyse_flechette import FlechetteSciKit, TreshAnalyse
from pprint import pprint

# Couleur Rouge = x3
# Couleur Vert = x2
# Couleur Noir = x1
# Couleur Centre Rouge = 50 pts
# Couleur Centre Vert = 25 pts


if __name__ == '__main__':

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
    flechettes = TreshAnalyse.get_flechettes(tresh)

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
