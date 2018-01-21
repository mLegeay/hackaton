from analyse_flechette import FlechetteSciKit, TreshAnalyse, polygone
from pprint import pprint

# Couleur Rouge = x3
# Couleur Vert = x2
# Couleur Noir = x1
# Couleur Centre Rouge = 50 pts
# Couleur Centre Vert = 25 pts


if __name__ == '__main__':

    polygones = [
        {
            'point': 1,
            'polygone': polygone([516, 157], [584, 190], [526, 393])
        },
        {
            'point': 2,
            'polygone': polygone([698,632], [648,650], [539, 440])
        },
        {
            'point': 3,
            'polygone': polygone([589, 632], [536, 610], [529, 442])
        },
        {
            'point': 4,
            'polygone': polygone([712, 340], [655,255], [537,406])
        },
        {
            'point': 5,
            'polygone': polygone([452, 151], [403,174], [513, 390])
        },
        {
            'point': 6,
            'polygone': polygone([752, 520], [748, 438], [545, 423])
        },
        {
            'point': 7,
            'polygone': polygone([483, 581], [436, 531], [515, 434])
        },
        {
            'point': 8,
            'polygone': polygone([369, 404], [396, 468], [506, 419])
        },
        {
            'point': 9,
            'polygone': polygone([369, 219], [354, 271], [506, 396])
        },
        {
            'point': 10,
            'polygone': polygone([735, 589], [754, 524], [544, 430])
        },
        {
            'point': 11,
            'polygone': polygone([354, 337], [367, 402], [504, 410])
        },
        {
            'point': 12,
            'polygone': polygone([369, 418], [354, 270], [506, 396])
        },
        {
            'point': 13,
            'polygone': polygone([746, 434], [713, 344], [542, 414])
        },
        {
            'point': 14,
            'polygone': polygone([354, 273], [353, 333], [504, 403])
        },
        {
            'point': 15,
            'polygone': polygone([698, 631], [734, 590], [543, 437])
        },
        {
            'point': 16,
            'polygone': polygone([396, 469], [434, 529], [509, 428])
        },
        {
            'point': 17,
            'polygone': polygone([594, 645], [647, 650], [534, 442])
        },
        {
            'point': 18,
            'polygone': polygone([653, 254], [596, 192], [531, 398])
        },
        {
            'point': 19,
            'polygone': polygone([483, 581], [535, 619], [521, 440])
        },
        {
            'point': 20,
            'polygone': polygone([513, 155], [454, 150], [518,390])
        },
        {
            'point': 21,
            'polygone': polygone([526, 393], [539, 440], [529, 442], [537,406], [513, 390], [545, 423], [515, 434], [506, 419], [544, 430])
        },
    ]
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

    kk.cases_rouges_plot()

    # Affiche les différences notables entre l'image 1 et image 50
    print("Affiche les différences notables entre l'image 1 et image 50")
    tresh = kk.diff_n(50, False)

    # print(type(tresh))
    # print(tresh.tolist())

    # On récupère les flechettes présentes sur l'image
    flechettes = TreshAnalyse.get_flechettes(tresh)

    for flechette, i in zip(flechettes, range(len(flechettes))):
        print(flechette._x)
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
