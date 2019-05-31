import pytumblr
from wolf_gen import (main_art)
from wolf_post import post2

import random
import time
import sys, select


loop = False
sleep = 60 # in min
master_counter = 0

print "++++++++++++++++++++++++++++++++++++++++++"
start = raw_input('Start auto gifs y/n ?: ')
print "++++++++++++++++++++++++++++++++++++++++++"
if start == "y":
	loop = True 
while loop == True:
	main_art()

	post2()
	
	random_time = random.randint(1 ,60) * sleep
 	print "++++++++++++++++++++++++++++++++++++++++++"
 	print "Made " + str (master_counter) + " .Gif"
	print "++++++++++++++++++++++++++++++++++++++++++"
	print "Press enter to quit..next post in "+ str (random_time/60) + " min"
	print "++++++++++++++++++++++++++++++++++++++++++"
	i, o, e = select.select( [sys.stdin], [], [], random_time )
	if (i):
		print "++++++++++++++++++++++++++++++++++++++++++"
  		print "Goodbye"
  		print "++++++++++++++++++++++++++++++++++++++++++"
  		loop = False
	else:
		print "++++++++++++++++++++++++++++++++++++++++++"
  		print "Making more art"
  		print "++++++++++++++++++++++++++++++++++++++++++"

  	master_counter = master_counter + 1