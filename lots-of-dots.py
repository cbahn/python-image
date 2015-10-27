import Image
import math
import random
import operator


#basic def of screen size
screen_size = (1280,800)

def random_color():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def is_in_range(p):
	return (0 <= p[0] and p[0] < screen_size[0] and 0 <= p[1] and p[1] < screen_size[1])
			

def color_all(color, region):
	for p in region:
		pixels[ p[0], p[1] ] = color;

color_list = [(212,133,41),(179,86,0),(88,66,51),(147,119,103),(240,235,193)]

def disk_region(x,y,r):
	region = [];
	for px in range(max(0,x-r-1),min(screen_size[0],x+r+1)):
		for py in range(max(0,y-r-1),min(screen_size[1],y+r+1)):
			if( (px-x)*(px-x) + (py-y)*(py-y) < r*r*random.random()*random.random() ):
				region.append( (px,py) )
	return region

def decimate(l,drop_chance):
	l_final = []
	for al in l:
		if( random.random() < drop_chance ):
			l_final.append(al)
	return l_final

def length( vec ):
	return math.sqrt( vec[0]*vec[0] + vec[1]*vec[1] )

def star_region():
	position = (random.randint(0,screen_size[0]),random.randint(0,screen_size[1]))
	power = random.randint(200,400);
	region = []
	while( power > 0):
		size = random.randint(int(.0*power),int(0.07 * power)) + random.randint(12,34)
		region = region +  disk_region(position[0],position[1],int(size*.7389))
		power -= size
		to_center = map(lambda x,y: x/2 - y, screen_size, position)
		length_to_center = length(to_center)
		to_center = map(lambda x: int(10*x/length_to_center), to_center)
		position = map(lambda x,y: x - y + random.randint(-45,45), position, to_center)
	return region


# main
img = Image.new( 'RGB', screen_size, (240,235,193)) # create a new black image
pixels = img.load() # create the pixel map

for _ in range(1500):
	color_all( random.choice(color_list), star_region() )
			
img.save('myim.bmp')

