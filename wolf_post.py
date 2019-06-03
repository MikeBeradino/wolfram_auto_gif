import pytumblr
import random 

def post2():
	print("++++++++++++++++++++")
	print("posting now")
	print("++++++++++++++++++++")         
	consumer_key = 'xxxxxxxxxxxxxx'
	consumer_secret = 'xxxxxxxxxxxxxx'
	token_key = 'xxxxxxxxxxxxxx' 
	token_secret = 'xxxxxxxxxxxxxx'


	client = pytumblr.TumblrRestClient(
		 	consumer_key,
         	consumer_secret,
         	token_key,
         	token_secret
         	)
	random_scale = random.randint(0,12)

	if random_scale == 0:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_1.gif","gifs/wolf_2.gif","gifs/wolf_1.gif","gifs/wolf_2.gif"])
	if random_scale == 1:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_2.gif","gifs/wolf_1.gif","gifs/wolf_2.gif","gifs/wolf_1.gif"])
	if random_scale == 2:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_2.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_l.gif"])
	if random_scale == 3:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= "gifs/wolf_1.gif")
	if random_scale == 4:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= "gifs/wolf_2.gif")
	if random_scale == 5:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_1.gif","gifs/wolf_2.gif"])
	if random_scale == 6:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_2.gif","gifs/wolf_1.gif"])
	if random_scale == 7:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_1.gif","gifs/wolf_1.gif"])
	if random_scale == 8:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_1.gif","gifs/wolf_1.gif","gifs/wolf_1.gif"])
	if random_scale == 9:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_2.gif","gifs/wolf_2.gif","gifs/wolf_2.gif"])
	if random_scale == 10:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_l.gif","gifs/wolf_r.gif"])
	if random_scale == 11:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_r.gif","gifs/wolf_r.gif","gifs/wolf_r.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_l.gif"])
	if random_scale == 12:
		client.create_photo('wolframrules', state="published", tags=["gif","cellular automata","generative art","python","gifs","art","digital art"], data= ["gifs/wolf_1.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_r.gif","gifs/wolf_r.gif","gifs/wolf_r.gif","gifs/wolf_l.gif","gifs/wolf_l.gif","gifs/wolf_l.gif"])

