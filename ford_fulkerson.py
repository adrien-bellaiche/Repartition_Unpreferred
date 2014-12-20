__author__ = 'MOITIE Roderic'

from Tools import Vertex, PrioQueue


class Graph(object):
    """
    Graphe represente par une liste de sommets
    """

    def __init__(self):
        self._vertices = []

    def add_vertex(self, v):
        self._vertices.append(v)

    def read(self, file_name):
        """
        Initialisation du graphe par lecture de fichier
        """
        f = open(file_name, 'r')
        for i in range(int(f.readline())):
            self.add_vertex(Vertex(i))
        while True:
            t = map(lambda x: float(x), f.readline().strip().split())
            if len(t) < 3:
                break
            s = self._vertices[int(t[0])]
            d = self._vertices[int(t[1])]
            add_edge(s, d, t[2])
        f.close()

    def print_graph(self):
        """
        Affichage du graphe
        """
        for v in self._vertices:
            print '[' + v.full_repr() + ']'

    def print_pred(self, pi):
        """
        Affichage des predecesseurs
        pi doit faire la meme taille que self._vertices
        """
        for v in self._vertices:
            print '[' + str(v) + ' <- ' + str(pi[v.label]) + ']'

    def save_correspondances(self, correspondance_name, text_name):
        corr_file = open(correspondance_name, 'r')
        corr_lines = corr_file.readlines()
        data_corr = {}
        for line in corr_lines:
            data = line.split(' ')
            data_corr[data[0]] = data[1] + ' ' + data[2].split('\n')[0]
        nparts = len(data_corr)
        save_file = open(text_name, 'w')
        for v in self._vertices:
            if v.label != 0:
                for edge in v.adjList:
                    if edge.direct and edge.flow == 1 and edge.neighbor.label != (len(self._vertices) - 1):
                        str1 = data_corr[str(((v.label - 1) % nparts) + 1)]
                        str2 = data_corr[str(((edge.neighbor.label - 1) % nparts) + 1)]
                        save_file.write(str1 + ' -> ' + str2 + '\n')
        save_file.close()
        corr_file.close()

    def __str__(self):
        return str(self._vertices)

    def improve_flow(self, n_init=0):
        """
        Amelioration du flot pour l'algorithme de Ford Fulkerson
        """
        pi = dict()  # Dictionnaire de predecesseurs
        prio = PrioQueue()  # file de priorite
        init = self._vertices[n_init]  # sommet de depart

        # Initialisation des distances a 0 sauf pour le sommet de depart
        for v in self._vertices:
            v.distance = 0.0
            pi[v.label] = None
            prio.offer(v)
        init.distance = float('inf')

        while prio.size() > 0:
            cour = prio.poll()
            for e in cour.adjList:
                # Par construction des arcs inverses, la capacite residuelle
                # est toujours capacite-flot
                delta = e.capacity - e.flow
                dist = min(cour.distance, delta)
                dest = e.neighbor
                if dist > dest.distance:
                    dest.distance = dist
                    pi[dest.label] = cour

        # Puits = dernier sommet
        no = len(pi) - 1
        flot = self._vertices[no].distance
        if flot == 0:
            return False

        # Il existe un chemin de la source vers le puits
        # Ameliorer le flot le long de ce chemin

        while no != 0:
            e1 = pi[no].get_edge_to(self._vertices[no])
            e2 = e1.sym
            e1.flow += flot
            e2.flow -= flot
            no = pi[no].label
        return flot > 0

    def ford_fulkerson(self, source=0):
        while self.improve_flow(source):
            pass


def add_edge(source, dest, weight):
    source.add_neighbor(dest, weight)


def execute_algorithm():
    g = Graph()
    g.read('ex.graph')
    g.ford_fulkerson()
    g.save_correspondances('correspondance.txt', 'out.txt')