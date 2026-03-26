"""
Auteur : Emmanuel Bissonnette
Date : 3/26/2026
Description: Petit outil de dessing qui retourne un fichier\
      eps en sauvegardant le tout realise avec turtle 


"""
#from PIL import Image
import turtle






#fonctions

def pen_setup():
    """
        description: Une fonction qui s'acctive au lancement et initialise la tortue du stylo avec\
              les bon parametres
        entrees : aucune
        sorties: cree une tortue qui sert de stylo
    """
    global pen
    pen = turtle.Turtle()
    pen.color("black","red")
    global pen_size
    pen_size=3
    pen.pensize(pen_size)
    pen.speed(10)

def border_setup():
    """
        description: Une fonction qui s'acctive au lancement et fait une bordure pour savoir ou dessine
        entrees : aucune
        sorties: cree une bordure graphique 
    """
    border = turtle.Turtle()
    border.hideturtle()
    border.pensize(3)
    border.speed(0)
    border.penup()
    border.setposition(-256,-256)
    border.pendown()
    for side in range(4):
        border.forward(512)
        border.left(90)

def click_pen_size_up(x,y):
    """
    description: une fonction qui sactive lorsque le bouton pen + est appuye cette fonction augmente la taille du crayon
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee
    sortie: la taille du crayon est augmentee.
    """
    global pen_size 
    pen_size += 1
    pen.pensize(pen_size)
   
def click_pen_size_down(x,y):
    """
    description: une fonction qui sactive lorsque le bouton pen - est appuye cette fonction diminue la taille du crayon
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee
    sortie: la taille du crayon est diminuee.
    """
    global pen_size 
    pen_size -=1
    pen.pensize(pen_size)
   

def click_save(x,y):
     """
    description: 
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee
    sortie: un fichier eps contenant le dessin de lutlisateur.
    """
     turtle.hideturtle() #Cette commande cache la tortue pour ne pas la voir apparaitre dans le ficher eps
     turtle.getscreen().getcanvas().postscript(file='img.eps')# Cette commande cree un fichier eps du canevas \
                                                                #get screen recupere lecran avec turtle get canvas \
                                                                #recupere lecran complet avec le fond a laide de tkinter\
                                                                #postscript converti et sauvegarde en post script le contenu de get screen et get canvas.

def click_pen_up(x,y):
    """
    description: Cette fonction s'active lorsque le bouton penup est appuye elle souleve le crayon(empeche decrire).
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee
    sortie: le crayon arrette d'ecrire.
    """
    pen.penup()#Une fonction qui souleve le stylo ou arrette decrire.

def click_pen_down(x,y):
    """
    description: Cette fonction s'active lorsque le bouton pendown est appuye elle depose le crayon(recomancer a ecrire).
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon recomance a ecrire.
    """
    pen.pendown()#Une fonction qui depose le stylo ou recommance a ecrire.

def click_behavior(x , y):
   """
    description: Cette fonction s'active losque le stylo est appuye et elle le telleporte au coordonne de la souris.
    entree: x,y sont utilise pour savoir ou est la souris et la suivre avec le stylo.
    sortie: Le crayon suit la souris.
    """
   pen.setposition(x,y)# Teleporte le stylo a lendroit du click avec les entree x,y
    
def click_eraser (x,y):
    """
    description: Cette fonction s'active lorsque le bouton eraser est appuye elle met le stylo en blanc pour effacer.
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon change de couleur et efface.
    """
    pen.color("white","red")#Change la trail du crayon tout en gardant le milleux rouge pour une meilleure visibilite.
    
def click_black(x,y):
    """
    description: Cette fonction s'active lorsque le bouton black est appuye elle met le stylo en noir pour ecrire.
    entree: x,y sont obligatoir avec la fonction onclick mais ne sont pas utilisee.
    sortie: le crayon change de couleur et ecrit
    """
    pen.color("black","red")

def set_up_button():
    """
    description: Cette fonction s'active des le lancement du code elle prend la liste turtle list et cree plusieur \
                    tortues avec les parametre dans cette meme liste soit nom ,fonction associee et coordonee \
    entree: Cette fonction na pas d'entree.
    sortie: Plusieur tortues et leur fonctionalitee.
    """
    turtle_list =[["pen+",click_pen_size_up,-200,-276], \
                    ["pen-",click_pen_size_down,-100,-276],["save",click_save,0,-276], \
                        ["pen up",click_pen_up,-200,276],["pen down",click_pen_down,-100,276],\
                            ["eraser",click_eraser,0,276],["Black",click_black,100,276]]  #Liste de bouton a ajouter. \
                                #Avec la strucure suivante nom, fonction a call ,x,y
    
    for i in range(7):#En fonction du nombre de bouton ou range le code cree des boutons avec les parametre contenu dans \ 
        #la liste turtle_list.

        turtle_text = turtle_list[i][0]#Extrait le texte de la variable avant quelle soit ecrasee par la prochaine commande.

        turtle_list[i][0] = turtle.Turtle()#Cree la tortue dans la variable qui est dans la liste tortue liste.

        turtle_list[i][0].shape("square")#Change la forme de la tortue pour un carree.

        turtle_list[i][0].speed(0)#Cette commande modifie la vitesse pour rendre le chargement du ui plus rapide.

        turtle_list[i][0].shapesize(2,3)#Cette commande change la taille de la tortue pour la rendre plus facile a cliker.

        turtle_list[i][0].penup()#Cette commande sert a faire en sorte que la tortue ne laisse pas de trace en changeant de postion

        turtle_list[i][0].setposition(turtle_list[i][2],turtle_list[i][3])#Cette commande modifie les coordonee de la tortue en la positionnant \
        # a lendroit designe dans la liste turtle_list.

        turtle_list[i][0].write(turtle_text,align="center",font=("Courier", 15, "bold"))#Chaque turtle ecrit le contenu de la variable avant quelle \
        #ecrasee donc turtle_text.

        turtle_list[i][0].color("")#Cache la turtle pour laisser place au texte plus tard.

        turtle_list[i][0].onclick(turtle_list[i][1]) #Cree le les touches du click et la fonction associe a chaque torute.
            

#initialisation des touches
turtle.setup(512,600)#Taille de lecran.
border_setup()
pen_setup()
pen.ondrag(click_behavior)#Permet de pouvoirs prendre et deplacer la torute pour dessiner.
set_up_button()


#main

input("")

