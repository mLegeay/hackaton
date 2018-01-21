

class Flechette(object):

    def __init__(self, x, y, width, height, volume):

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._volume = volume

        self._tete = (self._x+self._width, self._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self._volume

    def __str__(self):
        return 'Flechette({2}) xOrigine[{0}; {1}] sHauteur = {3} sLargueur = {4}'.format(self.x, self.y, self.volume, self.height, self.width)
