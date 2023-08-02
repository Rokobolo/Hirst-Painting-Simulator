import colorgram
import random
from turtle import Turtle, Screen


screen = Screen()
screen.colormode(255)
screen.title("Hirst Painting Simulator")
screen.setup(width=800, height=800)
my_turtle = Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")


def collect_rgb(file_name, colors):
    rgb_colors = []
    colors = colorgram.extract(file_name, colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors


def draw_dots():
    cor_y = -350
    dots = 15

    for x in range(dots):
        my_turtle.goto(-350, cor_y)
        for y in range(dots):
            my_turtle.dot(25, random.choice(color_list))
            my_turtle.forward(50)
        cor_y += 50


color_list = collect_rgb("nier.png", 12)
draw_dots()

screen.exitonclick()
