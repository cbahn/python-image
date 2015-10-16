import Image
import math
import random

#basic def of screen size
screen_size = (1280,800)

def random_color():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def is_in_range(p):
	return (0 <= p[0] and p[0] < screen_size[0] and 0 <= p[1] and p[1] < screen_size[1])
			

def color_all(color, region):
	for p in region:
		pixels[ p[0], p[1] ] = color;

def hh(i,j):
	result = []
	for (x,y) in template:
		new_pixel = (i*3 + x , j*3 + y)
		if is_in_range(new_pixel):
			result.append( new_pixel )
	return result

color_list = [ (0,179,88) ,(9,105,162), (255,140,0),(255,140,0), (80,80,1)]

# main
img = Image.new( 'RGB', screen_size, "black") # create a new black image
pixels = img.load() # create the pixel map
		
for a in range(-1, 1+(screen_size[0] / 3) ):
	for b in range(-1,1+(screen_size[1] / 3)):
		color_all(random_color(), hh(a, b))

img.save('myim.bmp')

