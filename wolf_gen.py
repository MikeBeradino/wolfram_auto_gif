try:
	import Image
except ImportError:
	from PIL import Image, ImageSequence,ImageDraw
import random 
from random import randint as rint
import argparse
import os
from resizeimage import resizeimage

outputfile = ""
random_scale= random.randint(10,100)
width = int(10)
height = int(10)
rulenumber = int(18)
scalefactor = int(1)

color_scale = int (10)

count = 0
color_count = 0

color_r = True
color_b = True
color_g = True

# Define colors of the output image
r = random.randint(0, 255) 
g = random.randint(0, 255) 
b = random.randint(0, 255) 
r1 = random.randint(0, 255) 
g1 = random.randint(0, 255) 
b1 = random.randint(0, 255) 
true_pixel = (r, g, b)
false_pixel = (r1, g1, b1)

## remove old files in frams dir	
filelist = [ f for f in os.listdir("frames") if f.endswith(".png") ]
for f in filelist:
    	os.remove(os.path.join("frames", f))

img2 = Image.new("RGBA", (width, height), (255, 255, 255,255))
draw = ImageDraw.Draw(img2)
for i in range(width/2):
	draw.rectangle((i,i,width-i,height-i), outline=(int(r-i),int(g-i),int(b)))
	draw.rectangle((width/2,height/2,width/2,height/2), outline=(int(r),int(g),int(b)))
img2.save("frames/0.png","PNG")
img2.save("frames/20.png","PNG")


# Generates a dictionary that tells you what your state should be based on the rule number and the states of the adjacent cells in the previous generation
def generate_rule(rulenumber):
	rule = {}
	for left in [False, True]:
		for middle in [False, True]:
			for right in [False, True]:
				rule[(left, middle, right)] = rulenumber%2 == 1
				rulenumber //= 2
	return rule

# Generates a 2d representation of the state of the automaton at each generation
def generate_ca(rule):
	ca = []
	# Initialize the first row of ca randomly
	ca.append([])
	for x in range(width):
		ca[0].append(bool(random.getrandbits(1)))

	# Generate the succeeding generation
	# Cells at the eges are initialized randomly
	for y in range(1,height):
		ca.append([])
		ca[y].append(bool(random.getrandbits(1)))
		for x in range(1, width-1):
			ca[y].append(rule[(ca[y-1][x-1], ca[y-1][x], ca[y-1][x+1])])
		ca[y].append(bool(random.getrandbits(1)))
	return ca

rule = generate_rule(rulenumber)
ca = generate_ca(rule)


#new = Image.new("RGBA", (width, height), (255, 255, 255,255))
new = Image.new("RGBA", (400, 400), (r1, g1, b1))
#img2 = Image.new("RGBA", (400, 400), (255, 255, 255,255))
draw2 = ImageDraw.Draw(new)
for i in range(400/2):
	draw2.rectangle((i,i,400-i,400-i), outline=(int(r-i*2),int(g-i*2),int(b)))
	draw2.rectangle((400/2,400/2,400/2,400/2), outline=(int(r),int(g),int(b)))




print("Placing pixels...")
for y in range(height):
	count = count + 1
	for x in range(width):
		color_count = color_count + 1
		
		
		if color_count == width:
			color_count = 0
			
			if r >= color_scale and color_r == True:
				r = r - (color_scale) 
			
			if r <= color_scale:
				color_r = False
			
			if color_r == False:
				r = r + (color_scale)
			
			if r > 255 - color_scale and color_r == False:
				color_r = True

			if g >= color_scale and color_g == True:
				g = g - (color_scale) 
			if g <= color_scale:
				color_g = False
			if color_g == False:
				g = g + (color_scale)
			if g > 255 - color_scale and color_g == False:
				color_g = True

			if b >= color_scale and color_b == True:
				b = b - (color_scale) 
			if b <= color_scale:
				color_b = False
			if color_b == False:
				b = b + (color_scale)
			if b > 255 - color_scale and color_b == False:
				color_b = True
			
		#new.putpixel((x, y), (r, g, b) 
			
			#if ca[int(x/scalefactor)][int(y/scalefactor)] 
				
			#else (r1, g1, b1))
			#else (255, 255, 255,0))
		#print(x,y)
		#new.save(args.outputfile+str (x)+".png",)


		#filename = 'pikachu.png'
		#ironman = Image.open(filename, 'r')
		#filename1 = 'bg.png'
		#bg = Image.open(filename1, 'r')
		#text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
		#text_img.paste(bg, (0,0))
		#text_img.paste(ironman, (0,0), mask=ironman)
		#text_img.save("ball.png", format="png")
		
		

		

		
		#new_image2 = image.resize((400, 400), Image.ANTIALIAS)

		
		
		
		#text_img = Image.new('RGBA', (400,400), (0, 0, 0, 0))
		
		#text_img.paste(img2, (0,0))
		#text_img.paste(image, (0,0), mask=image)
		#text_img.save("frames/"+outputfile+str (count)+"test.png", format="png")


		new.save("frames/"+outputfile+str (count)+".png")
		new.putpixel((x, y), (r, g, b) 
			if ca[int(y/scalefactor)][int(x/scalefactor)] 
			else (r1, g1, b1))
		#new.save(args.outputfile+str (x)+".png",)
		image = Image.open("frames/"+outputfile+str (count)+".png")
		
		new_image = image.resize((500, 500))
		new_image.save("frames/"+outputfile+str (count)+".png")
		new_image.save("frames/"+outputfile+str ((width*2)-count)+".png")

#new_image2.save("test2.png", format="png")

path, dirs, files = next(os.walk("frames"))
file_count = len(files)
image_var=[]
frames = []
frames_reverse = []
frames_left = []
frames_right = []

for x in range(file_count-1):
	
	image_file = ("frames/"+str (x)+'.png')
	
	new_frame = Image.open(image_file)
	frames.append(new_frame)
	
	transposed  = new_frame.transpose(Image.FLIP_TOP_BOTTOM)
	frames_reverse.append(transposed)


	left_90 = new_frame.rotate(90)
	left_90_small = left_90.resize((250,500), Image.ANTIALIAS)
	frames_left.append(left_90_small)
	
	right_90 = new_frame.rotate(270)
	frames_right.append(right_90)

frames[0].save("wolf_1.gif", save_all=True, append_images=frames[0:], duration=1, loop=0)
frames_reverse[0].save("wolf_2.gif", save_all=True, append_images=frames_reverse[0:], duration=1, loop=0)
frames_left[0].save("wolf_l.gif", save_all=True, append_images=frames_left[0:], duration=1, loop=0)
frames_right[0].save("wolf_r.gif", save_all=True, append_images=frames_right[0:], duration=1, loop=0)



print(file_count)
print("Saving image...")
#new.save(args.outputfile)
print("Done!")
