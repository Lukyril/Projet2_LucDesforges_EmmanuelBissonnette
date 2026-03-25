
#from PIL import Image
import turtle
#implementation initiale du pen
global pen
turtle.setup(512,600)

pen = turtle.Turtle()
pen.color("black","red")
global pen_size
pen_size=3
pen.pensize(pen_size)
pen.speed(10)


#fonctions
def click_pen_size_up(x,y):
    global pen_size 
    pen_size += 1
    pen.pensize(pen_size)
   
def click_pen_size_down(x,y):
    global pen_size 
    pen_size -=1
    pen.pensize(pen_size)
   

def click_save(x,y):
    turtle.getscreen().getcanvas().postscript(file='img.eps')

def click_pen_up(x,y):
    pen.penup()

def click_pen_down(x,y):
    pen.pendown()

def click_behavior(x , y):
   pen.setposition(x,y)
    
def click_eraser (x,y):
    pen.color("white","black")
def click_black(x,y):
    pen.color("black")

def set_up_button():
    turtle_list =[["pen+",click_pen_size_up,-200,-276], \
                    ["pen-",click_pen_size_down,-100,-276],["save",click_save,0,-276], \
                        ["pen up",click_pen_up,-200,276],["pen down",click_pen_down,-100,276],["eraser",click_eraser,0,276],["Black",click_black,100,276]]  #Liste de bouton a ajouter.
    
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

        turtle_list[i][0].onclick(turtle_list[i][1])
            

#initialisation des touches
pen.ondrag(click_behavior) 
set_up_button()
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

