import math
import turtle

def f(x):
    acc = ((5 * x + 2) ** 2) / (x ** 2 +2)
    return acc
def g(x):
    acc = (math.cos(2*x) / (math.cos(x)+2) **2)
    return acc

def find_maximum_f(upper_limit, lower_limit, delta_x):
    x = lower_limit
    maximum = f(x)
    while lower_limit <= x <= upper_limit:
        x = x + delta_x
        y = f(x)
        if y > maximum:
            maximum = y
    return maximum

def find_maximum_g(upper_limit, lower_limit, delta_x):
    x = lower_limit
    maximum = g(x)
    while lower_limit <= x <= upper_limit:
        x = x + delta_x
        y = g(x)
        if y > maximum:
            maximum = y
    return maximum

def find_minimum_f(upper_limit, lower_limit, delta_x):
    x = lower_limit
    minimum = f(x)
    while lower_limit <= x <= upper_limit:
        x = x + delta_x
        y = f(x)
        if y < minimum:
            minimum = y
    return minimum

def find_minimum_g(upper_limit, lower_limit, delta_x):
    x = lower_limit
    minimum = g(x)
    while lower_limit <= x <= upper_limit:
        x = x + delta_x
        y = g(x)
        if y < minimum:
            minimum = y
    return minimum

def graph_f(upper_limit, lower_limit, delta_x, turtle_name, margin_fraction):
    turtle_name = turtle.Turtle()
    side_margins = margin_fraction * (upper_limit - lower_limit)
    top_bottom_margins = margin_fraction * (top - bottom)
    turtle_name.penup()
    turtle_name.goto(lower_limit, f(lower_limit))
    turtle_name.color("blue")
    turtle_name.pendown()
    x = lower_limit
    while x <= upper_limit:
        x = x + delta_x
        y = f(x)
        turtle_name.goto(x,y)

def graph_g(upper_limit, lower_limit, delta_x, turtle_name, margin_fraction):
    turtle_name = turtle.Turtle()
    side_margins = margin_fraction * (upper_limit - lower_limit)
    top_bottom_margins = margin_fraction * (top - bottom)
    turtle_name.penup()
    turtle_name.goto(lower_limit, g(lower_limit))
    turtle_name.color("red")
    turtle_name.pendown()
    x = lower_limit
    while x <= upper_limit:
        x = x + delta_x
        y = g(x)
        turtle_name.goto(x,y)

def graph_both(upper_limit, lower_limit, delta_x, margin_fraction, turtle_name):
    turtle_name = turtle.Turtle()
    if find_minimum_f(upper_limit, lower_limit, delta_x) < find_minimum_g(upper_limit, lower_limit, delta_x):
        bottom = find_minimum_f(upper_limit, lower_limit, delta_x)
    if find_minimum_f(upper_limit, lower_limit, delta_x) > find_minimum_g(upper_limit, lower_limit, delta_x):
        bottom = find_minimum_g(upper_limit, lower_limit, delta_x)
    if find_maximum_f(upper_limit, lower_limit, delta_x) > find_maximum_g(upper_limit, lower_limit, delta_x):
        top = find_maximum_f(upper_limit, lower_limit, delta_x)
    if find_maximum_f(upper_limit, lower_limit, delta_x) < find_maximum_g(upper_limit, lower_limit, delta_x):
        top = find_maximum_g(upper_limit, lower_limit, delta_x)
    side_margins = margin_fraction * ((lower_limit * lower_limit + upper_limit * upper_limit) ** (1/2))
    top_bottom_margins = margin_fraction * ((bottom * bottom + top * top) ** (1/2))
    screen = turtle_name.getscreen()
    screen.setworldcoordinates(lower_limit - side_margins, bottom - top_bottom_margins, upper_limit + side_margins, top + top_bottom_margins)
    turtle_name.penup()
    x = lower_limit
    turtle_name.goto(lower_limit, g(lower_limit))
    turtle_name.pendown()
    turtle_name.color("red")
    while x <= upper_limit:
        y = g(x)
        turtle_name.goto(x,y)
        x = x + delta_x
    turtle_name.penup()
    x = lower_limit
    turtle_name.goto(lower_limit, f(lower_limit))
    turtle_name.pendown()
    turtle_name.color("blue")
    while x <= upper_limit:
        y = f(x)
        turtle_name.goto(x,y)
        x = x + delta_x
