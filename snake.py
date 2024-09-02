import pgzrun
import random

HEIGHT=800
WIDTH=800
TITLE="SNAKE GAME"

GO=False
Score=0
Time=45



def draw():
  screen.clear()
  screen.fill("green")
  fruit.draw()
  snake.draw()  
  


#unable to find smaller pngs
snake=Actor('snake')
fruit=Actor('fruit')
snake.pos=400,400
fruit.pos=random.randint(0,800),random.randint(0,800)

def time_up():
  global time
  if time==0:
    GO=True

def run_game():
  while GO=False:
    

pgzrun.go()