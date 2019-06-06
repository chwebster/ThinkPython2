import numpy as np
import Point1 as pt

# Calculate distance between two point objects
def distance(p1, p2):
    return np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# Move a rectangle object by vector (dx, dy)
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

# Instantiate a point object p and give it attributes x and y
p = pt.Point()
p.x = 3
p.y = 4
# Instantiate a point object q and give it attributes x and y
q = pt.Point()
q.x = 5
q.y = 6
print('p:', p)
print('q:', q)
# Calculate distance d between p and q
d = distance(p, q)
print('Distance between points is', d)

# Instantiate two new point objects a and b, specifying the attribute values at instantiation
a = pt.Point(2, 3)
b = pt.Point(4, 6)
print('a:', a)
print('b:', b)
# Calculate distance d between a and b
d = distance(a, b)
print('Distance between points is', d)

# Add a to b
print('a + b =', a + b)

# Add a to a tuple
print('a + (7, 8) =', a + (7, 8))

# Add a to an integer
print('a + 5 =', a + 5)

# Add a tuple to a:
print('(7, 8) + a =', (7, 8) + a)

# Add an integer to a:
print('5 + a =', 5 + a)

box = pt.Rectangle()
box.width = 10
box.height = 5
box.corner = pt.Point()
box.corner.x = 2
box.corner.y = 4

move_rectangle(box, 3, 1)
print('New corner is ', end = "")
pt.print_point(box.corner)

import chw_ex_ch14 as chw
chw.blah()
