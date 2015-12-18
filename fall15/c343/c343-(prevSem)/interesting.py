# interesting stuff

from turtle import *

def stuff():
    screen = getscreen()
    pencil = Turtle()
    pencil.ht()
    pencil.speed = 'fastest'
    pencil.up()
    for e in range(5,70,2):
        shape("turtle")
        pencil.stamp()
        pencil.forward(e)
        pencil.right(23)
    done()

stuff()