import json
import api_handler

i = 1
for friend in api_handler.get_friends(76189507):
	data = {'data': []}
	try:
		for group in api_handler.get_subscriptions(friend):
			data['data'].append(api_handler.get_posts(group))
			i = i + 1
			print(i)

		with open(str(friend) + '_TEXT.txt', 'a') as outfile:
			for text in data['data']:
				outfile.write(text)
			outfile.close()
	except:
		print('error')
		continue

