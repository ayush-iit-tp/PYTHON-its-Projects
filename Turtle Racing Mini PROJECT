import turtle
import time
import random
WIDTH, HEIGHT = 900, 900
COLORS =['red','green','blue','orange','magenta','black','cyan', 'brown','purple']

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Racing Turtle GameWorld!")
def get_number_of_racers():
    racers =0
    while True:
        racers = input("How many racers are there?(2-9): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a number...this time")
            continue
        if 2 <= racers < 10:
            return racers
        else:
            print("Please enter a number between 2 and 9...this time")

def create_turtles(colors):
        turtles = []
        spacingx = WIDTH // (len(colors)+1)
        for i,color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-WIDTH//2 + (i+1) * spacingx,-HEIGHT//2 + 20)
            racer.pendown()
            turtles.append(racer)

        return turtles
def race(colors):
    turtles = create_turtles(colors)

    while True:
            for racer in turtles:
                distance = random.randrange(1,20)
                racer.forward(distance)

                x, y = racer.pos()
                if y > (HEIGHT//2)-20:
                 return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(10)

'''it will slice the list of colors 
to number of racers entered
like this
[1, 2, 3, 4][:2]
means [1, 2] only
[1, 2, 3, 4][:3]
means [1, 2, 3] only
'''
''' Potential Speeds of turtles can vary from 0-10
fastest 0
fast 10
normal 6
slow 3
slowest 1
'''
'''
racer1 = turtle.Turtle()
racer1.penup()
racer1.shape('turtle')
racer1.color('blue')
racer1.speed(3)
racer1.forward(80)
racer1.left(90)
racer1.backward(150)
racer1.left(90)
racer1.backward(150)

racer2 = turtle.Turtle()
racer2.penup()
racer2.shape('turtle')
racer2.color('red')
racer2.speed(1)
racer2.backward(100)
racer2.right(90)
racer2.forward(250)
racer2.left(90)
racer2.forward(350)

racer3 = turtle.Turtle()
racer3.penup()
racer3.color('magenta')
racer3.shape('turtle')
racer3.speed(6)
racer3.forward(100)
racer3.right(90)
racer3.forward(150)
racer3.left(90)
racer3.backward(100)
'''

