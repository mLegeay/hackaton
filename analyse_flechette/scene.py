from os.path import exists


class FlechetteScene(object):

    CAM_TYPES = ['CAM-DROITE', 'CAM-FACE', 'CAM-HAUT']

    def __init__(self, fichier):
        self._scenes = list()

        for elem in FlechetteScene.CAM_TYPES:
            if exists('VIDEO-SRC/{0}/{1}'.format(elem, fichier)) is False:
                raise Exception('Manque {0} pour {1} !'.format(elem, fichier))

            self._scenes.append('VIDEO-SRC/{0}/{1}'.format(elem, fichier))

    @property
    def scenes(self):
        return self._scenes
