import Image
import math
import random

#basic def of screen size
screen_size = (1280,800)

number_bands = 14


def gradient( i ):
	return 1 + (screen_size[1]*(screen_size[0]/2 - abs(screen_size[0]/2 - i)) / screen_size[0])

# main
img = Image.new( 'RGB', screen_size, (238,232,213)) # create a new black image
pixels = img.load() # create the pixel map

for x in range(screen_size[0]):
	#number_bands = gradient(x)
	band_width = screen_size[1] / number_bands
	
	for y in range(screen_size[1]):
		if (y%band_width >= band_width*(y/band_width) / number_bands):
			pixels[x,y] = (42,161,152 )


img.save('stripes.bmp')

