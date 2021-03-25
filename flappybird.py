#modules
import turtle
import random
import math

#Customizing of Screen
wn = turtle.Screen()
wn.bgpic("flappy.gif")
wn.title("Flappy Bird")

#Registering the Shapes
turtle.register_shape("bird.gif")
turtle.register_shape("barrier.gif")

#Creating Flappy Bird
flappy = turtle.Turtle()
flappy.shape ("bird.gif")
flappy.speed(0) 
flappy.penup()
flappy.setposition(-100,0)

#Creating the barriers
barriers = []
for i in range(3):
	barriers.append(turtle.Turtle())
for barrier in barriers:
	barrier.shape("barrier.gif")
	barrier.speed(0)
	barrier.penup()

#barriers' initial position
barriers[0].setposition(300, random.randint(-150,150))
barriers[0].hideturtle()
barriers[1].setposition(550, random.randint(-150,150))
barriers[1].hideturtle()
barriers[2].setposition(800, random.randint(-150,150))
barriers[2].hideturtle()

#Flappy Bird Movements
def move_up():
   	 	global start, state
		state = False
		flappy_y = flappy.ycor()
		flappy_y += 30
		if flappy_y > 300:
			flappy.sety(300)
		else:
			flappy.sety(flappy_y)
		start = True 
		state = True

#End of the Game Prompter
def game_over():
    	score.clear()

	end_points = turtle.Turtle()
	end_points.color("black")
	end_points.write(points,False, align="center",font=("Arial",50,"bold"))
	end_points.hideturtle()

	end = turtle.Turtle()
	end.speed(0)
	end.color("black")
	end.penup()
	end.setposition(0,-50)
	end.write("GAME OVER",False, align="center",font=("Arial",30,"bold"))
	end.hideturtle()
	turtle.exitonclick()

#On key Function
def listen():
    	turtle.listen()
	turtle.onkey(move_up,"space")

#Barrier Vertical Movement
def up_down():
	for barrier in barriers:
		barrier.seth(90)
		barrier.speed(1)
		barrier.fd(random.randint(50,100))
		barrier.bk(random.randint(50,100))


state = True #True - Flappy is moving down; false if otherwise
start = False

#Startup
starting = turtle.Turtle()
starting.color("yellow")
starting.hideturtle()
while not start:
	starting.write("click space to start", False, align="center",font=("Arial",30,"normal"))
	starting.hideturtle()
	listen()
starting.clear()

#Scoreboard
points = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.setposition(0, 200)
score.write(points,False, align="center",font=("Arial",50,"bold"))
score.hideturtle()


#Main Game
while start:
	#up_down()
	while state:
		listen()
		flappy.speed(0)
		flappy_y = flappy.ycor()
		flappy_y -= 15
		flappy.sety(flappy_y)

		#incrementing speed
		increment = 5*(points/2)
		if increment >=40:
			x = 40
		else:
			x = increment
		#left shifting of barriers
		for barrier in barriers:
			barrier_x = barrier.xcor()
			barrier_x-=(10+x)
			barrier.speed(0)
			#Visibility of barrier as it enters the screen
			if barrier_x>250:
				barrier.hideturtle()
			else:
				barrier.showturtle()

			#Invisibility of barrier as it exits the screen
			if barrier_x <-250:
				barrier.hideturtle()
				barrier.setx(500)
				barrier.sety(random.randint(-150,150))
			else:
				barrier.setx(barrier_x)

			#up and down movement of barriers
			barrier_y = barrier.ycor()
			if flappy.xcor()+50<barrier_x:
				barrier_y+=random.randint(-20,20)
				if barrier_y<-150:
					barrier.sety(barrier_y+50)
				elif barrier_y>150:
					barrier.sety(barrier_y-50)
				else:
					barrier.sety(barrier_y)

			#Collision Checking
			if flappy.xcor()>(barrier_x-50) and flappy.xcor()<(barrier_x+50):
				if flappy.ycor()>barrier_y+35 or flappy.ycor()<barrier_y-32:
					state=False
					flappy.setposition(flappy.xcor()+90, -300)
					game_over()
			elif flappy.ycor()<-300:
					state=False
					game_over()
			elif barrier_x+50<flappy.xcor()<barrier_x+65+x:
				points+=1
				score.clear()
				score.write(points,False, align="center",font=("Arial",50,"bold"))
				score.hideturtle()