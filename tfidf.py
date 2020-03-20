from sklearn.feature_extraction.text import TfidfVectorizer
import api_handler

corpus = []

with open('76189507_TEXT.txt', 'r') as infile:
	corpus.append(infile.read())
	infile.close()

for friend in api_handler.get_friends(76189507):
	try:
		with open(str(friend) + '_TEXT.txt', 'r') as infile:
			corpus.append(infile.read())
			infile.close()
	except:
		continue

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names()

res = []
i = 0
with open('76189507_TEXT.txt', 'r') as infile:
	for word in infile.read().split(' '):
		try:
			index = words.index(word)
		except:
			print('error')
			continue
		print(i)
		i = i + 1
		if X.getrow(0).getcol(index) > 0.008:
			res.append(word)
	print(0)
	infile.close()

with open('76189507_TEXT.txt', 'w') as new:
	new.close()

with open('76189507_TEXT.txt', 'a') as outfile:
	for word in res:
		outfile.write(word + ' ')
	outfile.close()

i = 1
for friend in api_handler.get_friends(76189507):
	res = []
	try:
		with open(str(friend) + '_TEXT.txt', 'r') as infile:
			for word in infile.read().split(' '):
				try:
					index = words.index(word)
				except:
					continue
				if X.getrow(i).getcol(index) > 0.008:
					res.append(word)
			infile.close()

		with open(str(friend) + '_TEXT.txt', 'w') as new:
			new.close()

		with open(str(friend) + '_TEXT.txt', 'a') as outfile:
			for word in res:
				outfile.write(word + ' ')
			outfile.close()
		print(i)
		i = i + 1
	except:
		continue

# corpus = [
# 	'word word word word word word word word word word word word word word word word word rf word ',
# 	'word word word word ',
# 	'word word word word ',
# 	'word word word return return',
# 	'word word word return return',
# 	'word word word return return',
# 	'word word word return return',
# 	'word word word return return',
# ]
#
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# words = vectorizer.get_feature_names()
# for word in corpus[4].split(' '):
# 	index = words.index(word)
# 	print(word, X.getrow(4).getcol(index), X.getrow(4).getcol(index) > 0.69)
