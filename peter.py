import Image
import math
import random
import operator
from operator import add
from operator import floordiv

img = Image.open("asska.bmp")
pixels = img.load() # create the pixel map

# basic def of screen size
screen_size = img.size
num_centers = 3000


def random_color():
	return ( random.randint(0,255) , random.randint(0,255) , random.randint(0,255) )

def distance_squared( p1 , p2 ):
#	return max( abs(p1[0]-p2[0]), abs(p1[1]-p2[1]) )
#	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
	return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])

def random_point():
	return ( random.randint(0, screen_size[0]-1), random.randint(0, screen_size[1]-1))

def in_range( p ):
	return (-50 < p[0] and p[0] <= screen_size[0]+50 and -50 < p[1] and p[1] <= screen_size[1] + 50)

point_list = []
point_list_num = 0
for x in range(-100,100):
	for y in range(-100,100):
		maybe_add = ( int(17+30*x+15*y), int(8 + 25.9807621135*y) )
		if( in_range(maybe_add) ):
			point_list.append( ( maybe_add,point_list_num ) )
			point_list_num += 1
				

# point_list = [ ( random_point(), random_color()), (random_point(), random_color()), (random_point(), random_color()) ]

def closest_point( t, l ):
	best_distance = 200000000;
	valu = -1;
	for point_val in l:
		new_distance = distance_squared( point_val[0] , t )
		if (best_distance >= new_distance):
			best_distance = new_distance
			valu = point_val[1]
	return valu

# main


# (x,y) = img.size

#init list
sorted_list = [ [] for _ in range( num_centers ) ]

# place pixels into sorted_list
for x in range( screen_size[0] ):
	for y in range( screen_size[1] ):
		sorted_list[ closest_point( (x,y), point_list ) ].append( (x,y) )

for l in sorted_list:
	c = (0,0,0)
	count = 0
	for p in l:
		count += 1
		c = map(add, c, pixels[p[0],p[1]] )
	if (count > 0):
		c = map( floordiv, c, (count,count,count) )
		# print c
		for p in l:
			pixels[p[0], p[1]] = tuple(c)


img.save('hex_asska.bmp')

