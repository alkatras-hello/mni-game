import random
do_you_want_to_music = input("do you want to play music? (y/n): ")
import turtle
import time
import os
import threading
import sounddevice as sd
import soundfile as sf
import keyboard
import tkinter as tk
from tkinter import messagebox
screen = turtle.Screen()
screen.bgpic("road.gif")
asgore_score = 0
speed_boost = float(5)
speed_boost_dess = float(10)
screen.addshape("car.gif")
screen.addshape("dess.gif")
screen.setup(width=400, height=700)
dess = turtle.Turtle()
dess.shape("dess.gif")
dess.penup()
file_path_music = os.path.join(os.path.dirname(__file__), "asgore.mp3")
dess.goto(0, 60)
dess.pendown()
asgore = turtle.Turtle()
asgore.penup()
asgore.goto(0, 350)
asgore.shape("car.gif")
asgore.pendown()  
if do_you_want_to_music == "y":
     data, samplerate = sf.read(file_path_music)
     threading.Thread(target=sd.play, args=(data, samplerate), daemon=True).start()
elif do_you_want_to_music == "yes":
     data, samplerate = sf.read(file_path_music)
     threading.Thread(target=sd.play, args=(data, samplerate), daemon=True).start()
elif do_you_want_to_music == "n":
     print("ok, no music")
elif do_you_want_to_music == "no":
     print("ok, no music")
dess.speed(4)
screen.tracer(0)
dess.up()
asgore.up()
while True:
    dess_act = random.randint(1, 3)
    if dess_act == 1:
        dess.setheading(180)
        dess.forward(25)
    elif dess_act in (2, 3):
        dess.setheading(0)
        dess.forward(25)
        dess.setheading(270)
        dess.forward(40)

    asgore.setheading(270)
    asgore.forward(40)

    if asgore.distance(dess.position()) < 50:
        dess.hideturtle()
        messagebox.showinfo("WON!", "you kill dess, you win")
        break
    elif asgore.distance(dess.position()) < 60:
         dess.speed(4.5)
    elif asgore.distance(dess.position()) > 60:
            dess.speed(4.2)
    if dess.ycor() < -350:
            dess.goto(0, 60)   
    if asgore.ycor() < -350:
        asgore.goto(0, 350)
    asgore_score += 1
    speed_boost += 0.1
    speed_boost_dess += 0.1
   
    
    if keyboard.is_pressed("a"):
        asgore.setheading(180)
        asgore.forward(30)
        asgore.setheading(270)
        asgore.forward(20)
    elif keyboard.is_pressed("d"):
        asgore.setheading(0)
        asgore.forward(30)
        asgore.setheading(270)
        asgore.forward(20)
    elif keyboard.is_pressed("shift") and speed_boost > 0:
        asgore.speed(2)
        speed_boost -= 1
    elif keyboard.is_pressed("shift") and speed_boost_dess >= 0:
        dess.speed(4.7)
        speed_boost_dess -= 1
    elif speed_boost >= 5:
        speed_boost -= 1
    elif speed_boost_dess >= 10:
        speed_boost_dess -= 1
    elif keyboard.is_pressed("q"):
        break

    
   

    
    turtle.update()
    time.sleep(0.1)