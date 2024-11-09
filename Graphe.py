from primitives_piles_et_files import *

class Graphe:

    def __init__(self, sommets = [], aretes = []):
        # le nombre de sommets
        self.n = len(sommets)
        # notre matrice carrée ne contenant que des 0 et 
        # de dimension self.n
        self.m = [[0 for col in range(self.n)] for ligne in range(self.n)]
        # liste des noms des sommets
        self.nom = sommets
        # dico des indices des sommets
        self.num = { sommets[i] : i for i in range(len(sommets))}
        # on pose des arêtes éventuelles
        for d, a in aretes:
            # on récupère les indices
            i_d, i_a = self.num[d], self.num[a]
            # et on met à jour la matrice
            self.m[i_d][i_a] = self.m[i_a][i_d] = 1

    def ajoute_sommet(self, sommet):
        """ ajoute un sommet au graphe """
        # à la matrice
        for ligne in self.m:
            ligne.append(0)
        self.m.append([0 for col in range(self.n + 1)])
        # à l'effectif
        self.n += 1
        # à la liste
        self.nom.append(sommet)
        # au dico
        self.num[sommet] = self.n - 1
        
    def ajoute_arete(self, arete : tuple):
        """ ajoute une arête au graphe """
        a, d = arete
        # on récupère les indices
        i_d, i_a = self.num[d], self.num[a]
        # et on met à jour la matrice
        self.m[i_d][i_a] = self.m[i_a][i_d] = 1

    def supprime_arete(self, arete : tuple):
        """ supprime une arête au graphe"""
        a, d = arete
        # on récupère les indices
        i_d, i_a = self.num[d], self.num[a]
        # et on met à jour la matrice
        self.m[i_d][i_a] = self.m[i_a][i_d] = 0

    def supprime_sommet(self, sommet):
        """ supprime un sommet (et ses arêtes) au graphe """
        if sommet in self.nom:
            # on récupère l'indice de sommet
            i_s = self.num[sommet]
            # à la matrice
            for ligne in self.m:
                del ligne[i_s]
            # on supprime la ligne
            self.m.pop(i_s)
            # à l'effectif
            self.n -= 1
            # à la liste
            self.nom.remove(sommet)
            # mise à jour du dico des indices
            self.num = {self.nom[i] : i for i in range(self.n)}

    def voisins(self, s):
        """renvoie la liste d'ajacence de s"""

        # indice de s
        i = self.num[s]
        # ligne de la matrice [1, 1, 0, .. ,0, 1, 1]
        ligne = self.m[i]
        # col est un indice ligne(col) booléen (False si zéro)
        return [self.nom[col] for col in range(self.n) if ligne[col]]

    def dico_adjacence(self):
        return {s : self.voisins(s) for s in self.nom}

    def parcours_largeur(self, depart):
        # liste sommets marqués
        marques = [depart] # départ déjà marqué

        # chaine pour le parcours
        parcours = ''
        
        # une file vide
        f = File()

        # initialisation
        f.enfiler(depart)

        # tant que la file n'est pas vide
        while not f.est_vide():
            # on défile u
            u = f.defiler()
            # on l'a parcouru
            parcours += u
            # pour chaque sommet v adjacent au sommet u :
            for v in self.voisins(u):
                # si v n'est pas marqué
                if v not in marques:
                    # on marque v et on l'enfile
                    marques.append(v)
                    f.enfiler(v)

        return parcours

    def parcours_profondeur(self, depart):
        # liste sommets marqués
        marques = [depart] # départ déjà marqué

        # chaine pour le parcours
        parcours = ''
        
        # une pile vide
        p = Pile()

        # initialisation
        p.empiler(depart)

        # tant que la pile n'est pas vide
        while not p.est_vide():
            # on dépile u
            u = p.depiler()
            # on l'a parcouru
            parcours += u
            # pour chaque sommet v adjacent au sommet u :
            for v in self.voisins(u):
                # si v n'est pas marqué
                if v not in marques:
                    # on marque v et on l'empile
                    marques.append(v)
                    p.empiler(v)

        return parcours

    def parcours_profondeur_r(self, u, marques = []):
        # on marque u
        marques.append(u)
        print(u)
        # pour chaque sommet v adjacent au sommet u :
        for v in self.voisins(u):
            # si v n'est pas marqué
            if v not in marques:
                # Appel récursif sur v
                self.parcours_profondeur_r(v, marques)

    def degre(self, sommet):
        """ renvoie le degré d'un sommet """
        if sommet in self.nom:
            i_s = self.num[sommet]
            return sum(self.m[i_s])
        return 0
        
    def __repr__(self):
        # ligne de libellés des colonnes
        chaine = '  '
        for s in self.nom:
            chaine += s + ' '
        for i in range(self.n):
            chaine += '\n' + self.nom[i]
            for col in self.m[i]:
                chaine += ' ' + str(col)
                
        return chaine 
    
            
# # de 'A' à 'I'
# sommets = [chr(unicode) for unicode in range(ord('A'), ord('J'))]
# # les arêtes
# aretes = [('A', 'B'),
#           ('A', 'C'),
#           ('A', 'H'),
#           ('B', 'I'),
#           ('C', 'E'),
#           ('C', 'D'),
#           ('D', 'E'),
#           ('E', 'G'),
#           ('G', 'F'),
#           ('G', 'H'),
#           ('H', 'I'),
#           ('F', 'I')]
          
# g = Graphe(sommets, aretes)

# #g.ajoute_sommet('K')

# #g.ajoute_arete(('A', 'E'))
# #g.ajoute_arete(('B', 'C'))
# #g.ajoute_arete(('K', 'H'))
# #g.ajoute_arete(('K', 'B'))
# #g.ajoute_arete(('K', 'F'))

# #g.supprime_arete(('A', 'C'))
# #g.supprime_sommet('I')


