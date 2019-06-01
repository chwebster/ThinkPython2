import numpy as np
import Point1 as pt

def distance(p1, p2):
    return np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

p = pt.Point()
p.x = 3
p.y = 4

q = pt.Point()
q.x = 5
q.y = 6

d = distance(p, q)
print('Distance between points is', d)

box = pt.Rectangle()
box.width = 10
box.height = 5
box.corner = pt.Point()
box.corner.x = 2
box.corner.y = 4

move_rectangle(box, 3, 1)
print('New corner is ', end = "")
pt.print_point(box.corner)