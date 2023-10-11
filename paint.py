import pygame
import math

pygame.init()

screen = pygame.display.set_mode([600,800])
pygame.display.set_caption("Paint")

RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (148,0,211)
BLACK = (0,0,0)
GREY = (169,169,169)

pressed = False

red = False
blue = False
green = False
yellow = False
orange = False
purple = False
black = True
rubber = False
fill = False

file_created = False

grid = [
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    ]


def draw_board():
    line_thickness = 1
    for i in range(40):
        pygame.draw.line(screen, WHITE, (i*15,0), (i*15,600),line_thickness)
        pygame.draw.line(screen, WHITE, (0,i*15), (600, i*15),line_thickness)
    pygame.draw.line(screen, WHITE, (0,600), (600, 600),line_thickness)    

def add_to_grid():
    global red
    global blue
    global green
    global yellow
    global orange
    global purple
    global black
    global rubber
    global fill
    global file_created

    try:
        
        x,y = event.pos

        
        
        if x >= 40 and x <= 70 and y >= 650 and y <= 680:
            red = True
            blue = False
            green = False
            yellow = False
            orange = False
            purple = False
            black = False
            rubber = False

        elif x >= 120 and x <= 150 and y >= 650 and y <= 680:
            red = False
            blue = True
            green = False
            yellow = False
            orange = False
            purple = False
            black = False
            rubber = False

        elif x >= 200 and x <= 230 and y >= 650 and y <= 680:
            red = False
            blue = False
            green = True
            yellow = False
            orange = False
            purple = False
            black = False
            rubber = False

        elif x >= 280 and x <= 310 and y >= 650 and y <= 680:
            red = False
            blue = False
            green = False
            yellow = True
            orange = False
            purple = False
            black = False
            rubber = False

        elif x >= 360 and x <= 390 and y >= 650 and y <= 680:
            red = False
            blue = False
            green = False
            yellow = False
            orange = True
            purple = False
            black = False
            rubber = False

        elif x >= 440 and x <= 470 and y >= 650 and y <= 680:
            red = False
            blue = False
            green = False
            yellow = False
            orange = False
            purple = True
            black = False
            rubber = False

        elif x >= 520 and x <= 550 and y >= 650 and y <= 680:
            red = False
            blue = False
            green = False
            yellow = False
            orange = False
            purple = False
            black = True
            rubber = False

        elif x >= 200 and x <= 250 and y >= 700 and y <= 740:
            red = False
            blue = False
            green = False
            yellow = False
            orange = False
            purple = False
            black = False
            rubber = True

        
        if x >= 0 and x <= 600 and y >= 0 and y <= 600:
            x /= 15
            y /= 15
            positionX = math.floor(x)
            positionY = math.floor(y)


            if red == True:
                grid[positionY][positionX] = "R"
            if blue == True:
                grid[positionY][positionX] = "B"
            if green == True:
                grid[positionY][positionX] = "G"
            if yellow == True:
                grid[positionY][positionX] = "Y"
            if orange == True:
                grid[positionY][positionX] = "O"
            if purple == True:
                grid[positionY][positionX] = "P"
            if black == True:
                grid[positionY][positionX] = "K"
            if rubber == True:
                grid[positionY][positionX] = "0"
                
        
        if x >= 20 and x <= 70 and y >= 700 and y <= 740:
            for i in range(40):
                for j in range(40):
                    grid[i][j] = "0"

        if x >= 80 and x <= 130 and y >= 700 and y <= 740 and pressed != False:
            if file_created == False:
                global filename
                filename = input("What do you want the name of your file to be? ")
                file = open(filename, "w+")
                for i in range(40):
                    string1 = str("".join(grid[i]))
                    file.write(string1)
                file.close()
                print("Saved!")
                file_created = True
            else:
                file = open(filename, "w+")
                file.truncate(0)
                
                for i in range(40):
                    string2 = str("".join(grid[i]))
                    file.write(string2)
                
                file.close()
                print("Saved!")
                
            

        if x >= 140 and x <= 190 and y >= 700 and y <= 740 and pressed != False:
            if file_created == False:
                openfilename = input("What is the name of the file? ")
                file = open(openfilename, "r")
                for i in range(40):
                    for j in range(40):
                        char = file.read(1)
                        grid[i][j] = char
                file.close()
                filename = openfilename
                file_created = True
   
        
    except:
        pass

    """
    if x >= 260 and x <= 310 and y >= 700 and y <= 740:
        fill = True
        colours = [[red,"R"], [blue,"B"], [green,"G"], [yellow,"Y"], [orange,"O"], [purple,"P"], [black,"K"]]
        for i in range(40):
            for j in range(40):
                for k in colours:
                    if grid[i][j] != 0 and grid[i][j+1] != 0:
                        if grid[i][j] == "0" or k[1]:
                            grid[i][j] = k[1]
    """
    

def draw():
    for i in range(40):
        for j in range(40):
            if grid[i][j] == "R":
                pygame.draw.rect(screen,RED,((j*15),(i*15),15,15))
            if grid[i][j] == "B":
                pygame.draw.rect(screen,BLUE,((j*15),(i*15),15,15))
            if grid[i][j] == "G":
                pygame.draw.rect(screen,GREEN,((j*15),(i*15),15,15))
            if grid[i][j] == "Y":
                pygame.draw.rect(screen,YELLOW,((j*15),(i*15),15,15))
            if grid[i][j] == "O":
                pygame.draw.rect(screen,ORANGE,((j*15),(i*15),15,15))
            if grid[i][j] == "P":
                pygame.draw.rect(screen,PURPLE,((j*15),(i*15),15,15))
            if grid[i][j] == "K":
                pygame.draw.rect(screen,BLACK,((j*15),(i*15),15,15))

def draw_colour_buttons():
    red_button = pygame.draw.rect(screen, RED, (40,650, 30,30))
    blue_button = pygame.draw.rect(screen, BLUE, (120,650, 30,30))
    green_button = pygame.draw.rect(screen, GREEN, (200,650,30,30))
    yellow_button = pygame.draw.rect(screen, YELLOW, (280,650,30,30))
    orange_button = pygame.draw.rect(screen, ORANGE, (360,650,30,30))
    purple_button = pygame.draw.rect(screen, PURPLE, (440,650,30,30))
    black_button = pygame.draw.rect(screen, BLACK, (520,650,30,30))
                    
def clear_button():
    clear_font = pygame.font.Font("freesansbold.ttf",15)
    clearbutton = clear_font.render("Clear", True, (BLACK))
    pygame.draw.rect(screen, GREY, (20, 700, 50,40))
    screen.blit(clearbutton,(25,710))

def save_button():
    save_font = pygame.font.Font("freesansbold.ttf",15)
    savebutton = save_font.render("Save", True, (BLACK))
    pygame.draw.rect(screen, GREY, (80, 700, 50,40))
    screen.blit(savebutton,(85,710))

def open_button():
    open_font = pygame.font.Font("freesansbold.ttf",15)
    openbutton = open_font.render("Open", True, (BLACK))
    pygame.draw.rect(screen, GREY, (140, 700, 50,40))
    screen.blit(openbutton,(145,710))

def rubber_button():
    rubber_font = pygame.font.Font("freesansbold.ttf", 13)
    rubberbutton = rubber_font.render("Rubber", True, (BLACK))
    pygame.draw.rect(screen, GREY, (200, 700, 50, 40))
    screen.blit(rubberbutton,(202,710))

"""
def fill_button():
    fill_font = pygame.font.Font("freesansbold.ttf", 15)
    fillbutton = fill_font.render("Fill", True, (BLACK))
    pygame.draw.rect(screen, GREY, (260, 700, 50, 40))
    screen.blit(fillbutton,(265,710))
"""

running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or pressed == True:
            add_to_grid()
            pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False

    draw()
    draw_board()
    draw_colour_buttons()
    clear_button()
    save_button()
    open_button()
    rubber_button()
    #fill_button()
    pygame.display.update()

print("Ended")
