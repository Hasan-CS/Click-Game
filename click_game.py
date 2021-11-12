# a121_catch_a_turtle.py
#-----import statements-----
import random as r
import turtle as trtl
import leaderboard as lb
wn = trtl.Screen()
t = trtl.Turtle()

#-----game configuration----
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = wn.textinput("Hello", "Please enter your name: ")

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
  
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global leaderboard_file_name
  global score
  global t

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, t, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, t, score)


#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   
timer_up = False

#-----countdown turtle thing-----------
counter = trtl.Turtle()
counter.color("white")
counter.penup()
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
  
#-----finish----------------
manage_leaderboard()
wn.mainloop()
