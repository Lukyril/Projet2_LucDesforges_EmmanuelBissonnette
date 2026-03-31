"""
Auteur : Emmanuel Bissonnette
Date : 3/26/2026
Description: Petit outil de dessing qui retourne un fichier\
      eps en sauvegardant le tout realise avec turtle 


"""

import turtle
import app
from pathlib import Path

#fonctions

def pen_setup():
    """
        description: Une fonction qui s'acctive dans la fonction 
        final_controls_setup et initialise la tortue du stylo avec les 
        bon parametres    
        entrees : aucune
        sorties: cree une tortue qui sert de stylo
    """
    global pen
    #Initialise la tortue.
    pen = turtle.Turtle()
    #Change la couleur du crayon tout en gardant le milleux rouge pour
    #  une meilleure visibilite.
    pen.color("black","red")
    #Cette variable est utilise dans plusieur fonction je l'es donc mit en globale.
    global pen_size 
    pen_size=3
    #Change la taille initiale du crayon
    pen.pensize(pen_size)
    #Defini la vitesse de base du crayon.
    pen.speed(10)

def border_setup():
    """
        description: Une fonction qui s'acctive dans la fonctio 
        final_controls_setup et fait une bordure pour savoir ou dessine
        entrees : aucune
        sorties: cree une bordure graphique 
    """
    #Initialise la tortue.
    border = turtle.Turtle() 
    #Rend la tortue invisible .
    border.hideturtle()
    #Change la taille du crayon pour faire une bordure plus eppaise.
    border.pensize(3)
    #Change la vitesse de la tortue pour que le temps de chargment soit plus bas.
    border.speed(0)
    #Souleve le stylo pour ne pas que la tortue laisse des trace en allant au coin.
    border.penup()
    #Teleporte la tortue au coin de la bordure.
    border.setposition(-256,-256)
    #Depose le crayon pour que la tortue puisse faire la bordure.
    border.pendown()
    #Passe a travers les 4 cote dun carre pour les dessiner.
    for side in range(4):
        border.forward(512)
        border.left(90)

def click_pen_size_up(x,y):
    """
    description: une fonction qui sactive lorsque le bouton pen + est appuye 
    cette fonction augmente la taille du crayon
    entree: x,y sont obligatoir avec la fonction onclick mais 
    ne sont pas utilisee
    sortie: la taille du crayon est augmentee.
    """
    global pen_size 
    pen_size += 1
    pen.pensize(pen_size)
   
def click_pen_size_down(x,y):
    """
    description: une fonction qui sactive lorsque le bouton pen - 
    est appuye cette fonction diminue la taille du crayon
    entree: x,y sont obligatoir avec la fonction onclick mais 
    ne sont pas utilisee
    sortie: la taille du crayon est diminuee.
    """
    global pen_size 
    pen_size -=1
    pen.pensize(pen_size)
   

def click_save(x,y):
     """
    description: une fonction qui cree un fichier eps a partir du 
    dessin du joueur
    entree: x,y sont obligatoir avec la fonction onclick mais 
    ne sont pas utilisee
    sortie: un fichier eps contenant le dessin de lutlisateur.
    """
     #Reduit la taille de lecran pour ne recuperer que le dessins du joueur.
     turtle.setup(512,512) 
     #Cette commande cache la tortue pour ne pas la voir apparaitre
     # dans le ficher eps
     turtle.hideturtle() 
     #get screen recupere lecran avec turtle get canvas \
    #recupere lecran complet avec le fond a laide de tkinter\
    #postscript converti et sauvegarde en post script le contenu 
    # de get screen et get canvas
     screen = turtle.getscreen()
     canvas = screen.getcanvas()
     # Cette commande cree un fichier eps du canevas \
     canvas.postscript(file=Path(__file__).parent.parent / "input/eps/" / 'input.eps')
    # Remet lecran a sa taille initiale pour que les boutons soit accessible.                                            
     turtle.setup(512,600)
     app.save_convert()

def click_pen_up(x,y):
    """
    description: Cette fonction s'active lorsque 
    le bouton penup est appuye elle souleve le crayon(empeche decrire).
    entree: x,y sont obligatoir avec la fonction 
    onclick mais ne sont pas utilisee
    sortie: le crayon arrette d'ecrire.
    """
    #Une fonction qui souleve le stylo ou arrette decrire.
    pen.penup()

def click_pen_down(x,y):
    """
    description: Cette fonction s'active lorsque le bouton pendown est appuye elle depose le crayon(recomancer a ecrire).
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon recomance a ecrire.
    """
    #Une fonction qui depose le stylo ou recommance a ecrire.
    pen.pendown()

def click_behavior(x , y):
   """
    description: Cette fonction s'active losque le stylo est appuye et elle le telleporte au coordonne de la souris.
    entree: x,y sont utilise pour savoir ou est la souris et la suivre avec le stylo.
    sortie: Le crayon suit la souris.
    """
   # Teleporte le stylo a lendroit du click avec les entree x,y
   pen.setposition(x,y)
    
def click_eraser (x,y):
    """
    description: Cette fonction s'active lorsque le bouton eraser est appuye elle met le stylo en blanc pour effacer.
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon change de couleur et efface.
    """
    #Change la trail du crayon tout en gardant le milleux rouge 
    # pour une meilleure visibilite.
    pen.color("white","red")

def click_black(x,y):
    """
    description: Cette fonction s'active lorsque le bouton black est appuye elle met le stylo en noir pour ecrire.
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon change de couleur et ecrit
    """
    ##Change la trail du crayon tout en gardant le milleux 
    # rouge pour une meilleure visibilite.
    pen.color("black","red")

def set_up_button():
    """
    description: Cette fonction s'active dans la fonction final_controls_setupelle prend la liste turtle list et cree plusieur \
                    tortues avec les parametre dans cette meme liste soit nom ,fonction associee et coordonee \
    entree: Cette fonction na pas d'entree.
    sortie: Plusieur tortues et leur fonctionalitee.
    """
    #Liste de bouton a ajouter ,Avec la strucure suivante nom,
    #  fonction a call ,x,y
    turtle_list =[["pen+",click_pen_size_up,-200,-276], \
                    ["pen-",click_pen_size_down,-100,-276],["save",click_save,0,-276], \
                        ["pen up",click_pen_up,-200,276],["pen down",click_pen_down,-100,276],\
                            ["eraser",click_eraser,0,276],["Black",click_black,100,276]]  
    #En fonction du nombre de bouton ou range le code cree \
    # des boutons avec les parametre contenu dans la liste turtle_list.
    for i in range(7):
        #Extrait le texte de la variable avant quelle soit ecrasee par 
        # la prochaine commande
        turtle_text = turtle_list[i][0]
        #Cree la tortue dans la variable qui est dans la liste tortue liste.
        turtle_list[i][0] = turtle.Turtle()
        #Change la forme de la tortue pour un carree.
        turtle_list[i][0].shape("square")
        #Cette commande modifie la vitesse pour rendre le chargement 
        # du ui plus rapide.
        turtle_list[i][0].speed(0)
        #Cette commande change la taille de la tortue pour la rendre plus 
        # facile a cliker.
        turtle_list[i][0].shapesize(2,3)
        #Cette commande sert a faire en sorte que la tortue 
        # ne laisse pas de trace en changeant de postion
        turtle_list[i][0].penup()
        #Cette commande modifie les coordonee de la tortue en la positionnant \
        # a lendroit designe dans la liste turtle_list.
        turtle_list[i][0].setposition(turtle_list[i][2],turtle_list[i][3])
        #Chaque turtle ecrit le contenu de la variable avant quelle \
        #ecrasee donc turtle_text.
        turtle_list[i][0].write(turtle_text,align="center",font=("Courier", 15, "bold"))
        #Change la couleur de la turtle en transparent  pour laisser 
        # place au texte plus tard.
        turtle_list[i][0].color("")
        #Cree le les touches du click et la fonction associe a chaque torute.
        turtle_list[i][0].onclick(turtle_list[i][1]) 
            
def final_setup():
    """
    description: Call toute les fonction pour creer les boutons, linterface graphique, et le stylo\
                     elle initialise aussi le controle pour le stylo et la grosseur de lecran.
    entrees:aucune
    sorties:aucune
    
    """
    #Taille de lecran.
    turtle.setup(512,600)
    # Change le nom de la console tortle pour le nom du jeux
    turtle.title("Sketch a Turt")
    border_setup()
    pen_setup()
    #Permet de pouvoirs prendre et deplacer la torute pour dessiner.
    pen.ondrag(click_behavior)
    set_up_button()
#Fait en sorte que le code ne termine jamais 
input("")

