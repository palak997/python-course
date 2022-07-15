from turtle import *
speed('fastest')
colors = ['red','blue','pink','yellow','brown' ,'black ','green','voilet','orange']

for i in range (500):
    s = len (colors)
    c = colors[i % s]
    pencolor(c)
    forward(i + 10)
    left(360/s)
    for j in range (s):
        forward(200)
        left(360/s)