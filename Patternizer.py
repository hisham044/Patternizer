import turtle
import re
from math import floor #importing floor math for making calculated value to adjacent lower integer
 
# Function to validate
# hexadecimal color code .
def isValidHexaCode(str):
 
    # Regex to check valid
    # hexadecimal color code.
    regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
 
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if(str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

clr_codeBG = ''
clr_codePN = ''
clr_codeSP = ''

print('Welcome to Patternizer')
print('Lets Create Patterns!')     
#Taking Supportable input from user
Colour_dict = {0:'yellow', 1:'gold', 2:'orange', 3:'red', 4:'maroon', 5:'violet', 6:'magenta', 7:'purple', 8:'navy', 9:'blue', 10:'skyblue', 11:'cyan', 12:'turquoise', 13:'lightgreen', 14:'green', 15:'darkgreen', 16:'chocolate', 17:'brown', 18:'black', 19:'gray', 20:'white' , 21:'Color Code'}
print('Colour List:') 
for clr_num, clrrr in Colour_dict.items(): #assining 2 variables as key and value of the Colour_dict for Bg clr 
    print(clr_num, clrrr)#printing the number and colour 
clr_num = ' ' #variable to store bgcolour input #same variable that is assisned as one to store dict key
while clr_num not in Colour_dict: #checking if colour variable matches colour option in Colour_dict 
    clr_num = int(input('Choose a Bg Colour(Only num input(0-21): '))#taking colour input
    if clr_num == 21:
        while not isValidHexaCode(clr_codeBG):
            clr_codeBG = input('Enter a valid colour code(begin with #): ')

print('')
print('Colour List:')
for Penclr , clr_pen in Colour_dict.items(): #assining 2 variables as key and value of the Colour_dict for Pen/Stroke clr
    print(Penclr,clr_pen)
Penclr = ' '#variable to store the pen colour input #same variable that is assisned as one to store dict key
while Penclr not in Colour_dict: #checking if colour variable matches colour option in the Colour_dict 
    Penclr = int(input('Choose Stroke Colour(Only num input(0-21): '))#taking input
    if Penclr == 21:
        while not isValidHexaCode(clr_codePN):
            clr_codePN = input('Enter a valid colour code(begin with #): ')    

print('')
print('Colour List:')
for Shapeclr , clr_shape in Colour_dict.items():
    print(Shapeclr, clr_shape)
Shapeclr = ' '#variable to store the input
while Shapeclr not in Colour_dict: #checking if colour variable matches colour option in the option list
    Shapeclr = int(input('Choose Shape Colour(Only num input(0-21): '))#taking input
    if Shapeclr == 21:
        while not isValidHexaCode(clr_codeSP):
            clr_codeSP = input('Enter a valid colour code(begin with #): ')

print('')
print('Shape Option List:')
Shapes_dict = {'1': 'square', '2': 'triangle', '3': 'star', '4': 'flower' , '5': 'starcircle', '6': 'circleX', '7': 'turtle star' , '8':'4 side star','9':'rangoli flower','10':'circle rangoli','11':'squary', '12': 'octagon', '13': 'heart','14':'Batman'}
for shp_num, shape in Shapes_dict.items():
   print(shp_num, shape)
shp_num = ' '#variable to store the input
while shp_num not in Shapes_dict: #checking if shape input given matches shape option in the Shapes list
    shp_num = input('Choose a Shape (Only num input(1-14): ')#taking input

print('')
Size = 0 #sidelength multiplier variable
while Size < 1 or Size > 20: #input posibility only for numbers b/w 1-10
    Size = float(input('Enter Shape Size(Only num input(1-20): ')) #taking input as float to get input as numeric 

print('')
Distance = 0 #Gap Distance multiplier variable
while Distance < 1 or Distance > 20: #input posibility only for numbers b/w 1-10
    Distance = float(input('Enter Distance b/w Shapes(Only num input(1-20): ')) #taking input as float to get input as numeric 
print('')

#______________________________________________________________

#defining a function 'draw_shape' for drawing different shapes by using the variables
def draw_shape(shp_num, Penclr, Shapeclr, clr_codePN, clr_codeSP, Size,t):
    t.pendown()
    t.speed(0)
    xy = t.pos()#saving the initial position of the turtle
    if Penclr < 21:
        t.pencolor(Colour_dict[Penclr]) 
    if Shapeclr < 21:
        t.fillcolor(Colour_dict[Shapeclr])
    if Penclr == 21:
        t.pencolor(clr_codePN) 
    if Shapeclr == 21:
        t.fillcolor(clr_codeSP)
    
    t.begin_fill()

    if Shapes_dict[shp_num] == 'square':
        for i in range(4):
            t.forward(Size*4)           #1
            t.right(90)

    if Shapes_dict[shp_num] == 'triangle':
        for i in range(3):
            t.forward(Size*4)               #2
            t.left(120)

    if Shapes_dict[shp_num] == 'star':                             
        for i in range(5):#drawing a star           
            t.forward(Size*4)                #3  
            t.right(144)

    if Shapes_dict[shp_num] == 'flower':
        for i in range(50): 
            t.forward(Size*8)               #4
            t.right(155)            

    if Shapes_dict[shp_num] == 'starcircle':
        for i in range(77):
            t.forward(Size*6)               #5
            t.right(146)

    if Shapes_dict[shp_num] == 'circleX':
        for i in range(180):
            t.forward(Size*5)
            t.right(30)
            t.forward(Size)                 #6
            t.left(60)
            t.forward(Size*2.5)
            t.right(30)

            t.penup()
            t.setposition(xy)
            t.pendown()

            t.right(2)

    if Shapes_dict[shp_num] == 'turtle star':
        for i in range(36):
            t.forward(Size*6)               #7
            t.left(170)

    if Shapes_dict[shp_num] == '4 side star':
        for i in range(160):#4 side star
            t.right(i)
            t.circle(125,i)                 #8
            t.forward(i)
            t.right(90)

    if Shapes_dict[shp_num] == 'rangoli flower':
        for i in range(6):
            t.left(60)
            for i in range(6):              #9
                t.forward(Size*3)
                t.left(60)

    if Shapes_dict[shp_num] == 'circle rangoli': #circle2
        for i in range(30):
            t.circle(Size*3)   
            t.circle(Size*1)                #10
            t.left(30)   

    if Shapes_dict[shp_num] == 'squary':
        for i in range(200):   #squary
            t.forward(i)                    #11
            t.left(91)  

    if Shapes_dict[shp_num] == 'octagon':
        for i in range(8):
            t.forward(Size*3)               #12
            t.right(45)     

    def curve(): # Method to draw curve
        for i in range(200): # To draw the curve step by step
            t.right(1)
            t.forward(Size/11)                                            

    def draw_heart():  # Method to draw full Heart
        t.begin_fill()
        t.left(140)
        t.forward((Size/11)*113)
        curve() # Left Curve                            
        t.left(120)
        curve() # Right Curve
        t.forward((Size/11)*112)
        
    if Shapes_dict[shp_num] == 'heart':
        draw_heart()                        #13

    def draw_batman():
        bat = Size*3
        t.left(90)
        t.circle(bat,85)
        t.circle((bat/3.33),110)
        t.right(180)
        t.circle((bat/1.667),150)
        t.right(5)
        t.forward(bat/5)

        t.right(90)
        t.circle(-(bat/0.714285),140)
        t.forward(bat/1.25)
        t.right(110)
        t.circle((bat*2),30)
        t.circle((bat/1.667),100)
        t.left(50)
        t.forward(bat)

        t.right(145)
        t.forward(bat/1.667)
        t.left(55)
        t.forward(bat/2.5)
        t.left(55)
        t.forward(bat/1.667)
        t.right(145)
        t.forward(bat)
        t.left(50)

        t.circle((bat/1.667),100)
        t.circle((bat*2),30)
        t.right(110)
        t.forward(bat/1.25)
        t.circle(-(bat/0.714285),140)
        t.right(90)
        t.forward(bat/5)
        t.right(5)
        t.circle((bat/1.667),150)
        t.left(180)
        t.circle((bat/3.33),110)
        t.circle(bat,85)

    if Shapes_dict[shp_num] == 'Batman':
        draw_batman()                       #14


    t.end_fill()
    t.penup()
    t.setposition(xy)#moving the turtle back to the initial saved position
    t.setheading(0) #making the turtle point right/east so as to always move forward in right direction after each shape

#______________________________________________________________

t = turtle.Turtle() #Brought t variable acting as turtle


def Pattern_1(clr_num, shp_num, Penclr, Shapeclr, clr_codeBG, clr_codePN, clr_codeSP,Size, Distance):
    t = turtle.Turtle()
    turtle.tracer(0, 0) #made tracer 0,0 for not tracing the drawing so as to get instant pattern output
    if clr_num <21:
        turtle.bgcolor(Colour_dict[clr_num]) #assinging input Background clour
    if clr_num == 21:
        turtle.bgcolor(clr_codeBG)
    a = t.getscreen() 
    a.setup(width=910, height =620) #seted a fixed size for the opening up turtle graphics screen

    shape_distance = Distance*22 #the distance between two  shapes
    width = floor((900/(Size + shape_distance)) + 1)#calculating the no.of shapes that could draw in a row,so that the width of the scren is completely utilised and saving the data in the variable width
    height = floor((600/(Size + shape_distance)) + 1)#calculating the no.of shapes that could draw in a coloum,so that the height of the scren is completely utilised and saving the data in the variable height

    t.speed(0)
    t.penup()
    t.goto(-430,280) #starting position set to left corner of the opening up turtle graphics screen

    for y in range(height): #repeatation of rows drawing    
        for i in range(width): #repetation of shape drawing 
            draw_shape(shp_num= shp_num, Penclr= Penclr, Shapeclr=Shapeclr,clr_codePN=clr_codePN, clr_codeSP=clr_codeSP, Size = Size, t=t)#calling the function for drawing shapes
            t.forward(shape_distance) #giving gap between shapes
        t.backward(shape_distance * width)#returning to the left of the screen
        t.right(90)#going to next row
        t.forward(shape_distance)
        t.left(90)

Pattern_1(clr_num, shp_num, Penclr, Shapeclr, clr_codeBG, clr_codePN, clr_codeSP,Size, Distance)
turtle.textinput('To Continue:','Go Back to Patternizer') #popup message for minimizing screen

a = t.getscreen()  #asking user's satisfaction on pattern and asking for new inputs if needed to modify
change_yn = ''
while change_yn == 'n' or change_yn != 'y':
    change_yn = input('Did you like the Pattern? (y/n): ')
    if change_yn == "n":
        a.clear()
        Parameters = {'0':'BgClr', '1':'Penclr', '2':'Shapeclr', '3':'Shape', '4':'Size', '5':'Distance'}
        print('Parameters: ')
        for pm_num, pm in Parameters.items():
            print(pm_num,pm)  
        pm_num = input('Which parameter do you want to change: ')
        if Parameters[pm_num] == 'BgClr':
            print('')
            print('Colour List:') 
            for clr_num, clrrr in Colour_dict.items(): 
                print(clr_num, clrrr)
            clr_num = ' ' 
            while clr_num not in Colour_dict: 
                clr_num = int(input('Choose a Bg Colour(Only num input(0-21): '))
            if clr_num == 21:
                clr_codeBG = ''
                while not isValidHexaCode(clr_codeBG):
                    clr_codeBG = input('Enter a valid colour code(begin with #): ')
            
        if Parameters[pm_num] == 'Penclr':
            print('')
            print('Colour List:') 
            for Penclr , clr_pen in Colour_dict.items(): 
                print(Penclr,clr_pen)
            Penclr = ' '
            while Penclr not in Colour_dict: 
                Penclr = int(input('Choose Stroke Colour(Only num input(0-21): '))  
                if Penclr == 21:
                    clr_codePN = ''
                    while not isValidHexaCode(clr_codePN):
                        clr_codePN = input('Enter a valid colour code(begin with #): ')             

        if Parameters[pm_num] == 'Shapeclr':
            print('')
            print('Colour List:') 
            for Shapeclr , clr_shape in Colour_dict.items():
                print(Shapeclr, clr_shape)
            Shapeclr = ' '
            while Shapeclr not in Colour_dict: 
                Shapeclr = int(input('Choose Shape Colour(Only num input(0-21): '))
                if Shapeclr == 21:
                    clr_codeSP = ''
                    while not isValidHexaCode(clr_codeSP):
                        clr_codeSP = input('Enter a valid colour code(begin with #): ')

        if Parameters[pm_num] == 'Shape':
            print('')
            print('Shape Option List:')
            for shp_num, shape in Shapes_dict.items():
                print(shp_num, shape)
            shp_num = ' '
            while shp_num not in Shapes_dict: 
                shp_num = input('Choose a Shape (Only num input(0-14): ')
        if Parameters[pm_num] == 'Size':
            Size = 0 
            while Size < 1 or Size > 20: 
                Size = float(input('Enter Shape Size(Only num input(1-20): ')) 
        if Parameters[pm_num] == 'Distance':
            Distance = 0 
            while Distance < 1 or Distance > 20: 
                Distance = float(input('Enter Distance b/w Shapes(Only num input(1-20): ')) 
        turtle.clear()
        t.clear()
        Pattern_1(clr_num, shp_num, Penclr, Shapeclr, clr_codeBG, clr_codePN, clr_codeSP,Size, Distance)
        

    if change_yn == "y":
        print('Thank you')

turtle.done() 
#______________________________________________________________
