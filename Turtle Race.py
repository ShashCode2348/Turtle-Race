from turtle import *
from random import randint

dan = Turtle()
dan.color('darkgoldenrod')
dan.speed(0)
dan.penup()
dan.goto(-150,190)

for counter in range(17):
  dan.write(counter,align='center')
  dan.right(90)
  dan.forward(10)
  for counter in range(42):
    dan.pendown()
    dan.forward(5)
    dan.penup()
    dan.forward(5)
  dan.backward(430)
  dan.left(90)
  dan.forward(20)
dan.color('gold')
  
a = Turtle()
a.shape('turtle')
a.color('darkolivegreen')

a.penup()
a.goto(-170,155)
a.pendown()
a.color('red')
for turn in range(72):
  a.right(5)
for turn in range(72):
  a.left(5)
  
b = Turtle()
b.shape('turtle')
b.color('darkolivegreen')

b.penup()
b.goto(-170,120)
b.pendown()
b.color('blue')
for turn in range(72):
  b.right(5)
for turn in range(72):
  b.left(5)
  
c = Turtle()
c.shape('turtle')
c.color('darkolivegreen')

c.penup()
c.goto(-170,85)
c.pendown()
c.color('springgreen')
for turn in range(72):
  c.right(5)
for turn in range(72):
  c.left(5)
  
d = Turtle()
d.shape('turtle')
d.color('darkolivegreen')

d.penup()
d.goto(-170,50)
d.pendown()
d.color('darkgreen')
for turn in range(72):
  d.right(5)
for turn in range(72):
  d.left(5)
  
e = Turtle()
e.shape('turtle')
e.color('darkolivegreen')

e.penup()
e.goto(-170,15)
e.pendown()
e.color('cyan')
for turn in range(72):
  e.right(5)
for turn in range(72):
  e.left(5)
  
f = Turtle()
f.shape('turtle')
f.color('darkolivegreen')

f.penup()
f.goto(-170,-20)
f.pendown()
f.color('darkred')
for turn in range(72):
  f.right(5)
for turn in range(72):
  f.left(5)
  
g = Turtle()
g.shape('turtle')
g.color('darkolivegreen')

g.penup()
g.goto(-170,-55)
g.pendown()
g.color('darkorange')
for turn in range(72):
  g.right(5)
for turn in range(72):
  g.left(5)
  
h = Turtle()
h.shape('turtle')
h.color('darkolivegreen')

h.penup()
h.goto(-170,-90)
h.pendown()
h.color('magenta')
for turn in range(72):
  h.right(5)
for turn in range(72):
  h.left(5)
  
i = Turtle()
i.shape('turtle')
i.color('darkolivegreen')

i.penup()
i.goto(-170,-125)
i.pendown()
i.color('indigo')
for turn in range(72):
  i.right(5)
for turn in range(72):
  i.left(5)
  
j = Turtle()
j.shape('turtle')
j.color('darkolivegreen')

j.penup()
j.goto(-170,-160)
j.pendown()
j.color('saddlebrown')
for turn in range(72):
  j.right(5)
for turn in range(72):
  j.left(5)
  
while a.xcor() < 170 and b.xcor() < 170 and c.xcor() < 170 and d.xcor() < 170 and e.xcor() < 170 and f.xcor() < 170 and g.xcor() < 170 and h.xcor() < 170 and i.xcor() < 170 and j.xcor() < 170:
  a.forward(randint(0,5))
  b.forward(randint(0,5))
  c.forward(randint(0,5))
  d.forward(randint(0,5))
  e.forward(randint(0,5))
  f.forward(randint(0,5))
  g.forward(randint(0,5))
  h.forward(randint(0,5))
  i.forward(randint(0,5))
  j.forward(randint(0,5))
