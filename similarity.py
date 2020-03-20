import api_handler
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial import distance


def cos(a, b):
	return 1 - distance.cosine(a, b)


def make_vector(data):
	vector = []
	for word in words:
		vector.append(data.count(word))
	return vector


friends = api_handler.get_friends(76189507)
corpus = []

with open('backup_STEMMED/76189507_TEXT.txt', 'r') as infile:
	corpus.append(infile.read())
	infile.close()

for friend in friends:
	try:
		with open('backup_STEMMED/' + str(friend) + '_TEXT.txt', 'r') as infile:
			corpus.append(infile.read())
			infile.close()
	except:
		continue

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
Y = X.todense()
Y = Y.getA()
words = vectorizer.get_feature_names()
diction = {}
users_words = []

for i in range(len(corpus)):
	word_array = []
	indexes = {}
	for j in range(Y.shape[1]):
		indexes[j] = Y[i][j]
	k = 0
	for key, value in sorted(indexes.items(), key=lambda item: item[1], reverse=True):
		if k == 30:
			break
		k += 1
		word_array.append(words[key])
	users_words.append(word_array)

for i in range(len(corpus) - 1):
	diction['vk.com/id' + str(friends[i])] = [cos(X.todense()[0], X.todense()[i + 1]), users_words[i + 1]]


i = 0
for key, value in sorted(diction.items(), key=lambda item: item[1][0], reverse=True):
	print("%s: %s, %s" % (key, value[0], value[1]))
	i += 1
