from os.path import exists
from glob import glob


class FlechetteScene(object):

    CAM_TYPES = ['CAM-FACE']  # 'CAM-HAUT', 'CAM-DROITE',

    def __init__(self, fichier):
        self._fichier = fichier
        self._scenes = list()

        for elem in FlechetteScene.CAM_TYPES:
            if exists('VIDEO-SRC/{0}'.format(fichier)) is False:
                raise Exception('Manque {0} pour {1} !'.format(elem, fichier))

            self._scenes.append('VIDEO-SRC/{0}'.format(fichier))

    @property
    def scenes(self):
        return self._scenes

    @property
    def face(self):
        return 'VIDEO-SRC/{0}'.format(self._fichier)

    @property
    def haut(self):
        return 'VIDEO-SRC/{0}'.format(self._fichier)

    @property
    def droite(self):
        return 'VIDEO-SRC/{0}'.format(self._fichier)

    @staticmethod
    def get_scenes():
        """

        :rtype: list[FlechetteScene]
        """

        scenes = list()
        fichiers_cam_face = glob('VIDEO-SRC/CAM-FACE/*.mp4')

        for fichier in fichiers_cam_face:
            scenes.append(FlechetteScene(fichier.split('/')[-1]))

        return scenes

    def connect_url(self):
        return '192.168.10.2:554/'