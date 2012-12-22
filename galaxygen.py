import math
import random

totalStars = 10000
numSpiralStars = totalStars/2
numInnerStars = totalStars/4
numAmbientStars = totalStars/4

#Barred Spiral constants used in all passes - Real pain to change
A = 1.0
B = 0.25
N = 4.1

#Increase to widen spirals. Each pass uses a different width.
width = 0.50

#Increase to make more rotations in the spirals - Radians
length = 2.3
increment = length*math.pi/numSpiralStars
t = 0

#Spirals creates the dense spirals and bar
for s in range(numSpiralStars):
  
    t = t+increment
    tan = B * math.tan(t / (2*N))
    x = A * math.cos(t) / math.log(math.fabs(tan))
    #Gives us varying distance
    x = x + width*x*(random.random() - 0.5)
    #Enlarges the coordinates to galactic proportions 
    x = x * 100000
    y = A * math.sin(t) / (math.log(math.fabs(tan)))
    y = y + width*y*(random.random() - 0.5)
    y = y * 100000
    #Creates arms - 4 arms is kind of cluttered. Left it for ambient and inner so they are less defined.
    r = random.random()
    if r < 0.5:
        print x, y
#    elif r < 0.5:
#        print -x, y
#    elif r < 0.75:
#        print x, -y
    else:
        print -x, -y

#Inner core - Makes a smaller "galaxy" to fill in center
width = 0.9
increment = length*math.pi/numInnerStars
t = 0
for i in range(numInnerStars):
    t = t+increment
    tan = B * math.tan(t / (2*N))
    x = A * math.cos(t) / math.log(math.fabs(tan))
    x = x + width*x*(random.random() - 0.5)
    x = x * 15000
    y = A * math.sin(t) / math.log(math.fabs(tan))
    y = y + width*y*(random.random() - 0.5)
    y = y * 15000
    r = random.random()
    if r < 0.25:
        print x, y
    elif r < 0.5:
        print -x, y
    elif r < 0.75:
        print x, -y
    else:
        print -x, -y

#Ambient Stars - Passes over original spiral with a wider less dense spiral
#Longer spiral adds some fade out like real galaxies have
length = 2.6
width = 1.1
increment = length*math.pi/numAmbientStars
t = 0
for s in range(numAmbientStars):
    t = t+increment
    tan = B * math.tan(t / (2*N))
    x = (A * math.cos(t)) / (math.log(math.fabs(tan)))
    x = x + width*x*(random.random() - 0.5)
    x = x * 100000
    y = A * math.sin(t) / math.log(math.fabs(tan))
    y = y + width*y*(random.random() - 0.5)
    y = y * 100000
    r = random.random()
    if r < 0.25:
        print x, y
    elif r < 0.5:
        print -x, y
    elif r < 0.75:
        print x, -y
    else:
        print -x, -y
