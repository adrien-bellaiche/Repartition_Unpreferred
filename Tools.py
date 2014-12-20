__author__ = 'moitiero'


class Vertex(object):
    """
    Classe representant les sommets
    """
    """
    Variables de classe pour les couleurs de marquage
    """
    WHITE = 0
    GREY = 1
    BLACK = 2

    def __init__(self, label, distance=0):
        """
        Constructeur
        """
        self.label = label  # nom du sommet
        self.distance = distance  # distance du sommet a l'origine
        self.adjList = []  # liste d'adjacence
        self.mark = Vertex.WHITE  # marque

    def __lt__(self, v):
        """
        teste si le sommet est < a un autre sommet
        """
        return self.distance < v.distance

    def __gt__(self, v):
        """
        teste si le sommet est > a un autre sommet
        """
        return self.distance > v.distance

    def __str__(self):
        return str(self.label) + '(' + str(self.distance) + ')'

    def __repr__(self):
        return str(self.label) + '(' + str(self.distance) + ')'

    def full_repr(self):
        """
        Representation complete : sommet + voisins
        """
        return str(self.label) + ' (' + str(self.distance) + ') -> ' + str(self.adjList)

    def add_neighbor(self, v, cap):
        """
        Ajoute un voisin au sommet
        """
        e1 = Edge(v, cap)
        # Ajoute l'arc inverse
        e2 = Edge(self, cap, flow=cap, direct=False, sym=e1)
        e1.sym = e2
        self.adjList.append(e1)
        v.adjList.append(e2)

    def get_edge_to(self, v):
        """
        Retourne l'arc pointant vers v
        """
        for e in self.adjList:
            if e.neighbor.label == v.label:
                return e
        return None


class Edge(object):
    """
    Classe representant les arcs
    """

    def __init__(self, neigh, cap, flow=0, direct=True, sym=None):
        self.neighbor = neigh
        self.capacity = cap
        self.flow = flow
        self.direct = direct
        self.sym = sym

    def __repr__(self):
        c1 = ('-' if self.direct else '<')
        c2 = ('>' if self.direct else '-')
        return c1 + '--{' + str(self.flow) + '/' + str(self.capacity) + '}--' + c2 + str(self.neighbor.label)


class PrioQueue(object):
    """
    File de priorite
    """

    def __init__(self):
        self._queue = []

    def offer(self, v):
        """
        Ajoute un sommet a la file
        """
        self._queue.append(v)

    def poll(self):
        """
        Extrait le sommet de valeur maximale de la file
        """
        x = max(self._queue)
        self._queue.remove(x)
        return x

    def size(self):
        """
        Nombre d'elements de la file
        """
        return len(self._queue)

    def __str__(self):
        return str(self._queue)


if __name__ == "__main__":
    p = PrioQueue()
    p.offer(Vertex('a', 12))
    p.offer(Vertex('b', 5))
    p.offer(Vertex('z', 8))
    while p.size() > 0:
        print p.poll()
