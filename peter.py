import Image
import math
import random
import operator



# basic def of screen size
screen_size = (1280,800)

def random_color():
	return ( random.randint(0,255) , random.randint(0,255) , random.randint(0,255) )

def distance_squared( p1 , p2 ):
	return (p1[0]-p2[0])^2 + (p1[1]-p2[1])^2

def random_point():
	return ( random.randint(0, screen_size[0]-1), random.randint(0, screen_size[1]-1))

# point_list = [ ( random_point(), 0), (random_point(), 1), (random_point(), 2) ]

point_list = [ ( (0,0), 0), (screen_size,1) ]

def closest_point( t, l ):
	best_distance = 200000;
	valu = -1;
	for point_val in l:
		new_distance = distance_squared( point_val[0] , t )
		if best_distance > new_distance:
			best_distance = new_distance
			valu = point_val[1]
	return valu
		

# main
img = Image.new( 'RGB', screen_size) # create a new black image
pixels = img.load() # create the pixel map

print closest_point( (10,10), point_list )

for x in range( screen_size[0] ):
	for y in range( screen_size[1] ):
		if (closest_point( (x,y), point_list ) == 0):
			pixels[x,y] = random_color()
img.save('peter.bmp')

