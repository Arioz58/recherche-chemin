import pygame as pg
from pygame.locals import *
from Graphe import *

pg.init()

f = pg.display.set_mode((960,720))
pg.display.set_caption("Graphe")
# notre graphe instance de la Classe Graphe
g = Graphe()

lettre_ord = ord('A')

# dico de nos sommets (sous la from de 'key(lettre) : Rect')
sommets = {}

# liste de tuple des sommets étant liée par des aretes
aretes = []

# permet de choisir les deux sommet qu'on veut lier
start = False
target = False

# police de text
text_font = pg.font.SysFont('comic Sans', 30)

while True:
    pg.display.flip()
    f.fill((220,220,220))

    # si le nombre de sommet est > 1 car sinon aucune arete possible
    if len(sommets) > 1:
        # pg.draw.line(f, (255,255,255), sommets[0].center, sommets[1].center, 3) # on dessine une arete
        for arete in aretes:
            pg.draw.line(f, (0,0,0), arete[0].center, arete[1].center, 3)

    # on parcours la liste de sommets et les redessine
    for nom_sommet in sommets:
        pg.draw.circle(f, (180,180,180), sommets[nom_sommet].center , 20) # on dessine un premier cercle
        pg.draw.circle(f, (0,0,0), sommets[nom_sommet].center , 20, 5) # puis on dessine son contour en noir
        f.blit((text_font.render(nom_sommet, 0, (0,0,0))), (sommets[nom_sommet].centerx - 10, sommets[nom_sommet].centery - 23))

    #gestion des evenements
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit() # permet de pouvoir quiter avec la croix de la fenetre
        if event.type == MOUSEMOTION:
            xmouse, ymouse = event.pos
            mouse_hb = pg.Rect(xmouse, ymouse, 15, 12)
        
        # on recpuere les touches cliquer via la souris
        mouse_pressed = pg.mouse.get_pressed()
        if mouse_pressed[0]: # si clique gauche
            if mouse_hb.collidelistall(list(sommets.values())): # on test si on clique sur un sommet et on utilise la methode collidelistall() pour bouger qu'un seul sommet a la fois
                print(f"on deplace deplace {g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]}!") # on affiche dans le terminal le sommet qu'on deplace
                sommets[g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]].center = xmouse, ymouse # on place le sommet au coordonnées de la souris grace a la clé (Lettre du sommet)
            elif lettre_ord <= ord("Z"): # sinon on en place un. (Z pour ne pas depasser 25 sommet)
                print(f"sommet poser au position x : {xmouse} et y : {ymouse}")
                sommets[chr(lettre_ord)] = pg.Rect(xmouse - 20, ymouse - 20, 40, 40) # on ajoute des rect dans une liste de sommets
                g.ajoute_sommet(chr(lettre_ord)) # suppose ici que l'utilisateur ne mettra pas plus de 25 sommet (car on vas de A à Z)
                lettre_ord += 1 # on avance d'une lettre
                print(g) # on affiche dans le terminal
        
        if mouse_pressed[1]:
            if mouse_hb.collidelistall(list(sommets.values())):
                print(f"on supprime le sommet {g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]}!") # on affiche dans le terminal le sommet supr
                nom_sommet_supr = g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]
                g.supprime_sommet(g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]])
                del sommets[nom_sommet_supr]
                print(g) # on affiche dans le terminal
        
        if mouse_pressed[2]: # si clique droit
            # si on a pas choisi notre premier sommet
            if not start: 
                if mouse_hb.collidelistall(list(sommets.values())):
                    print(f"le 1er sommet choisi est {g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]}") # on affiche dans le terminal pour plus de lisibilitée
                    nom_sommet1 = g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]] # on stock le nom de notre sommet choisi
                    rect_sommet1 = sommets[g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]] # on stock le rect de notre sommet choisi
                    start = True # start devient True pour ne plus verifier la condition
            
            # si on a pas choisi notre second sommet
            elif not target:
                if mouse_hb.collidelistall(list(sommets.values())):
                    print(f"le 2eme sommet choisi est {g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]}")
                    nom_sommet2 = g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]
                    rect_sommet2 = sommets[g.nom[mouse_hb.collidelistall(list(sommets.values()))[0]]]
                    target = True # target devient True pour ne plus verifier la condition
            
            # si les deux bouléen sont verifier
            if target and start:
                if (rect_sommet1, rect_sommet2) in aretes:
                    aretes.remove((rect_sommet1, rect_sommet2))
                    aretes.remove((rect_sommet2, rect_sommet1))
                    g.supprime_arete((nom_sommet1, nom_sommet2))
                    print(f"arete supprimer entre les sommets {nom_sommet1} et {nom_sommet2}!")
                    nom_sommet1, nom_sommet2 = "", "" # on reinitialise nos variable 
                    start, target = False, False # et nos bouléens
                    print(g) # on affiche dans le terminal
                else:
                    g.ajoute_arete((nom_sommet1, nom_sommet2)) # on remplace par 1
                    aretes.append((rect_sommet1, rect_sommet2)) # on rajoute dans la liste des aretes (du sens de l'origine vers la cible)
                    aretes.append((rect_sommet2, rect_sommet1)) # on rajoute dans la liste des aretes (du sens de la cible vers l'origine)
                    print(f"arete crée entre les sommets {nom_sommet1} et {nom_sommet2}!") # on affiche dans les terminal l'arete crée
                    nom_sommet1, nom_sommet2 = "", "" # on reinitialise nos variable 
                    start, target = False, False # et nos bouléens
                    print(g) # on affiche dans le terminal
        
        if event.type == KEYDOWN:
            if event.key == K_c:
                sommets.clear()
                aretes.clear()
                g = Graphe()
                lettre_ord = ord('A')
    
    # affichage des intructions
    pg.draw.rect(f, (100,100,100), (0,540,960,180))
    f.blit((text_font.render("CLIQUE GAUCHE POUR POSER UN SOMMET", 0, (255,255,255))), (10,550))
    f.blit((text_font.render("CLIQUE DROIT POUR POSER UNE ARETE ENTRE 2 SOMMETS", 0, (255,255,255))), (10,585))
    f.blit((text_font.render("CLIQUE MOLETTE POUR SUPRIMER UN SOMMET", 0, (255,255,255))), (10,620))