class Polygone(object):

    def __init__(self, coordonnees):
        """
        Liste de coordonnée sous forme de tuple
        :param coordonnees:
        """
        self._coordonnees = coordonnees

    def inside_polygon(self, x, y):
        """
        Vérifie si une coordonnée x, y est dans le polygone
        """
        n = len(self._coordonnees)
        inside = False
        p1x, p1y = self._coordonnees[0]
        for i in range(1, n + 1):
            p2x, p2y = self._coordonnees[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside