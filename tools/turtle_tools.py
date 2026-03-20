import turtle


#implementation de la grille hardcoded




#function
def click_behavior(x , y):
    pass
def Grid_maker_coo():
    coordinate_grid = [[[0]*2]*64]*64
    pixel_top_left_corner = [-256,-256]
    pixel_bottom_right_corner = [-248,-248]
    coordinates = [pixel_top_left_corner, pixel_bottom_right_corner]
    #coordinate_grid[0] = coordinates
    for i in range(64):
        #coordinate_grid.append([]*64)
        for j in range(63):
            pixel_top_left_corner[0] += 8
            pixel_top_left_corner[1] += 8
            pixel_bottom_right_corner[0] += 8
            pixel_bottom_right_corner[1] += 8
            coordinates = [pixel_top_left_corner, pixel_bottom_right_corner]
            print(j+1)
            coordinate_grid[i][j+1] = coordinates
    print(coordinate_grid)

            
            


#initialisation des touches
turtle.onclick(click_behavior)
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
Grid_maker_coo()


input("")

