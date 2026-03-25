
#from PIL import Image
import turtle
#implementation initiale du pen
global pen
turtle.setup(512,600)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(10)
#setting up the button turtles



save_button = turtle.Turtle()
#pen_image = open("C:\Users\utilisateur\school\Programation 1\Projet2_LucDesforges_EmmanuelBissonnette\Ressources\lowrezbrush.gif","r")
#img  = Image.open("C:\Users\utilisateur\school\Programation 1\Projet2_LucDesforges_EmmanuelBissonnette\Ressources\lowrezbrush.gif") 
#pen.shape(img)

#fonctions
def click_pen_up():
    pen_size += 1
    pen.pensize(pen_size)

def click_behavior(x , y):
   pen.setposition(x,y)
    
     


turtle_list =[[0,-200,-275], \
                [0,-100,-275],[0,0,-275]]  #Liste de bouton a ajouter.
turtle_list[0][0] = pen_size_up_button = "pen+" #Fixe le texte  que doivent afficher les tortues.
turtle_list[1][0] = pen_size_down_button = "pen-"
turtle_list[2][0] = save_button ="save"
for i in range(3):#En fonction du nombre de bouton ou range le code cree des boutons avec les parametre contenu dans \ 
    #la liste turtle_list.

    turtle_text = turtle_list[i][0]#Extrait le texte de la variable avant quelle soit ecrasee par la prochaine commande.

    turtle_list[i][0] = turtle.Turtle()#Cree la tortue dans la variable qui est dans la liste tortue liste.
    print(turtle_list[i][0])
    turtle_list[i][0].hideturtle()#Cache la turtle pour laisser place au texte plus tard.

    turtle_list[i][0].shape("square")#Change la forme de la tortue pour un carree.

    turtle_list[i][0].speed(0)#Cette commande modifie la vitesse pour rendre le chargement du ui plus rapide.

    turtle_list[i][0].shapesize(2,3)#Cette commande change la taille de la tortue pour la rendre plus facile a cliker.

    turtle_list[i][0].penup()#Cette commande sert a faire en sorte que la tortue ne laisse pas de trace en changeant de postion

    turtle_list[i][0].setposition(turtle_list[i][1],turtle_list[i][2])#Cette commande modifie les coordonee de la tortue en la positionnant \
    # a lendroit designe dans la liste turtle_list.

    turtle_list[i][0].write(turtle_text,align="center",font=("Courier", 15, "bold"))#Chaque turtle ecrit le contenu de la variable avant quelle \
    #ecrasee donc turtle_text.
        

#initialisation des touches
pen.ondrag(click_behavior)
pen_size_up_button.onclick(click_pen_up)
#initialisation de la bordure
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
#main


input("")

