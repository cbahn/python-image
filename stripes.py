import Image
import math
import random

#basic def of screen size
screen_size = (1280,800)

number_bands = 14


def gradient( i ):
	return 1 + (screen_size[1]*(screen_size[0]/2 - abs(screen_size[0]/2 - i)) / screen_size[0])

# main
# img = Image.new( 'RGB', screen_size, (238,232,213)) # create a new black image
img = Image.open("truck.bmp")
pixels = img.load() # create the pixel map

for x in range( img.size[0] ):
	for y in range( img.size[1] ):
		if( random.randint(0,3) == 0):
			pixels[x,y] = (0,0,0)

img.save('stripes.bmp')

