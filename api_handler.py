import requests

def get_friends(id):
	r = requests.get('https://api.vk.com/method/friends.get?user_id=' + str(id) + '&access_token=fdc9dce6fdc9dce6fdc9dce6e0fda6a4e1ffdc9fdc9dce6a3ff2a4ce0ceff0e91a53947&v=5.103')
	return r.json()['response']['items']

def get_subscriptions(id):
	r = requests.get('https://api.vk.com/method/users.getSubscriptions?user_id=' + str(id) + '&access_token=fdc9dce6fdc9dce6fdc9dce6e0fda6a4e1ffdc9fdc9dce6a3ff2a4ce0ceff0e91a53947&v=5.103')
	return r.json()['response']['groups']['items']

def get_posts(id):
	r = requests.get('https://api.vk.com/method/wall.get?owner_id=-' + str(id) + '&count=100&access_token=fdc9dce6fdc9dce6fdc9dce6e0fda6a4e1ffdc9fdc9dce6a3ff2a4ce0ceff0e91a53947&v=5.103')
	hypertext = ''
	for item in r.json()['response']['items']:
		hypertext = hypertext + '\n\r' + item['text']
	return hypertext