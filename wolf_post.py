import pytumblr

def post2():         
	consumer_key = 'RUaWiNZrnI4hrEGRV17NQr6DibEzJmBgSSWQOWBVfR0vL0Ugdw'
	consumer_secret = 'v0iRisi0uGqgx9To3IP6kAs1umy8wzWx8ffwJ2vjcYoy3qbWe4'
	token_key = 'CZYKEzCT8nZJfhC9vxFgMwzNbgREBeT8pjp0JbFraGWiwndDTt' 
	token_secret = '4CO4oEhgrqVzTkQrLRfNKlhfU7rboOYyh72bpN0wQkBEPVqVLr'

	client = pytumblr.TumblrRestClient(
		 	consumer_key,
         	consumer_secret,
         	token_key,
         	token_secret
         	)
	client.create_photo('wolframrules', state="published", tags=["gif"], data= ["wolf_1.gif","wolf_2.gif","wolf_1.gif","wolf_2.gif"])
post2()