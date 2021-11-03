# a121_catch_a_turtle.py
#-----import statements-----
import random as r
import turtle as trtl
wn = trtl.Screen()
t = trtl.Turtle()

#-----game configuration----
wn.bgcolor("#1C1C1C")
t.color("red")
t.shape("circle")
t.penup()
t.speed(0)

trtl.penup()
trtl.hideturtle()
trtl.goto(-200, 200)
trtl.color("white")

score = 0
play = True
font_setup = ("Arial", 20, "normal")

#-----game functions--------
def move():
    t.stamp()
    color_list = ["red", "purple", "light green", "orange", "yellow"]
    background_list = ["black", "light blue"]
    size_list = ["1", "2", "3"]
    randX = r.randint(-200, 200)
    randY = r.randint(-200, 200)

    b_color = r.choice(background_list)
    what_color = r.choice(color_list)
    what_size = r.choice(size_list)
    
    wn.bgcolor(b_color)
    t.color(what_color)
    t.shapesize(int(what_size))
    t.setposition(randX, randY)

def score_for_circle(x,y):
  global score 
  global play
  if play == True:
    score += 1
    trtl.clear()
    trtl.write("Score: " + str(score),font=font_setup)
    move()

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   
timer_up = False

#-----countdown turtle thing-----------
counter = trtl.Turtle()
counter.color("white")
counter.goto(-50, 200)

#-----countdown-----------
def countdown():
  global timer, timer_up
  global play
  counter.clear()
  counter.hideturtle()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    play = False
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
countdown()
while play == True:
  t.onclick(score_for_circle)
if score >= 48:
  print("You scored " + str(score) + "!")
  print("I award you a trophy for beating my high score")
elif score >= 35:
  print("You scored " + str(score) + "!")
  print("You scored 35 or more! Congratulations, you win :)")
else:
  print("game over :(")
  print("You scored " + str(score))

#-----finish----------------
wn.mainloop()
