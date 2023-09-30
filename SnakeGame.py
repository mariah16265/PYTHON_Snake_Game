import turtle
import time
import random

delay = 0.1
queue = []

# Calculate the score and high score
pen = turtle.Turtle()
pen.shape('square')
pen.penup()
pen.speed(0)
pen.color('White')

pen.hideturtle()
pen.goto(0, 210)
pen.write("Score: 0    High score: 0   ", align='center', font=('Arial', 25, 'bold'))

# First, we create the snake window
window = turtle.Screen()
window.bgcolor('Black')
window.title('Snake_Game')
window.setup(width=600, height=500)
window.tracer(0)

# Next, we will create the snake head
Snake_Head = turtle.Turtle()
Snake_Head.speed(0)
Snake_Head.shape('circle')
Snake_Head.color('Beige')
Snake_Head.penup()
Snake_Head.goto(0, 0)  # by default it is in the center of the screen
Snake_Head.direction = 'stop'

# Next, we will create the snake food
Snake_Food = turtle.Turtle()
Snake_Food.speed(0)
Snake_Food.shape('circle')
Snake_Food.color('green')
Snake_Food.penup()
Snake_Food.goto(0, 150)  # by default it is in the center of the screen

# Rest of your code...



########################################################################
# Then , we will create all functions that we need to make snake move
def Move_Snake():
    if Snake_Head.direction == 'up':
        y = Snake_Head.ycor()
#It then updates the snake's head's y-coordinate by adding 10 units to it. 
#This effectively moves the snake's head 10 units upward on the screen, creating the illusion of the snake moving up.        
        Snake_Head.sety(y + 10)
# checks if the snake is moving "down," and if so, it decreases the y-coordinate by 10 units (y - 10), 
#moving the snake down.        
    if Snake_Head.direction == 'down':
        y = Snake_Head.ycor()
        Snake_Head.sety(y - 10)
#checks if the snake is moving "left," and if so, it decreases the x-coordinate by 10 units (x - 10), moving the snake left.        
    if Snake_Head.direction == 'left':
        x = Snake_Head.xcor()
        Snake_Head.setx(x - 10)
#checks if the snake is moving "right," and if so, it increases the x-coordinate by 10 units (x + 10), moving the snake right.        
    if Snake_Head.direction == 'right':
        x = Snake_Head.xcor()
        Snake_Head.setx(x + 10)


def go_up():
    Snake_Head.direction = 'up'


def go_down():
    Snake_Head.direction = 'down'


def go_left():
    Snake_Head.direction = 'left'


def go_right():
    Snake_Head.direction = 'right'


def Food_Collision():
    if Snake_Head.distance(Snake_Food) < 15:  # I choose 10 or 15 based on the incremental that we use to make the snakehead move
        # If a collision is detected, this line randomly relocates the food to a new position within the specified range.
        # The random.randint() function is used to generate random x and y coordinates for the food, 
        # ensuring it appears somewhere on the game screen.
        Snake_Food.goto(random.randint(-290, 290), random.randint(-249, 249))
        Snake_body = turtle.Turtle()  # after eating the food, the snake becomes bigger so I create one more turtle and add all in the list
        Snake_body.speed(0)
        Snake_body.shape('circle')
        Snake_body.color('yellow')
        Snake_body.penup()
        queue.append(Snake_body)
        return True
    return False



def Border_Collision():
    # Border collision
    if Snake_Head.xcor() > 290 or Snake_Head.xcor() < -290 or Snake_Head.ycor() > 249 or Snake_Head.ycor() < -249:
        time.sleep(1)
        Snake_Head.goto(0, 0)
        Snake_Head.direction = 'stop'
        for segment in queue:
            segment.goto(1000, 1000)
        queue.clear()
        return True

    return False
def Body_Collision():
    # body collisions
    for segment in queue:
        if segment.distance(Snake_Head) < 10:  # overlapping
            time.sleep(1)
            Snake_Head.goto(0, 0)
            Snake_Head.direction = 'stop'
            for segment in queue:
                segment.goto(1000, 1000)
            queue.clear()
            return True
    return False


def Add_Snake_Body():
    # add body to the snake because i don't know the length so i iterate from the last one in the list
    for i in range(len(queue) - 1, 0, -1):
        if i % 5 == 0:
            queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
            queue[i].color('green')
            continue
        queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
    if len(queue) > 0:
        queue[0].goto(Snake_Head.xcor(), Snake_Head.ycor())



# after that , i want to direct the snake head by using the keyboard so i should use keyboard bindings  so we use listen function in order to listen to the keypress
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')

####################################################################################
    # Game loop
score = 0
High_Score = 0
while True:

    window.update()
    Move_Snake()
    if Food_Collision():
        score += 10
        High_Score += 10
        if score > High_Score:
            High_Score = score
        pen.clear()
        pen.write('Score:{}    High score:{}  '.format(score, High_Score), align='center', font=('Arial', 25, 'bold'))

    if Body_Collision() or Border_Collision():
        score = 0
        pen.clear()
        pen.write('Score:{}    High score:{}  '.format(score, High_Score), align='center', font=('Arial', 25, 'bold'))
    time.sleep(delay)
    Add_Snake_Body()


# this keep the window open
window.mainloop()
