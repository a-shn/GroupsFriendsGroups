from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet
from nltk import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_wordnet_pos(treebank_tag):
	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	# elif treebank_tag.startswith('R'):
	# 	return wordnet.ADV
	else:
		return ''


def lemmatize(words):
	lemmatizer = WordNetLemmatizer()
	lemmatized = []
	pos_tags = pos_tag(words)
	i = 0
	for token, temp in zip(words, pos_tags):
		token_corr = temp[0].lower()
		pos = temp[1]
		print(pos)
		print(get_wordnet_pos(pos))
		if get_wordnet_pos(pos) != '':
			lemm = lemmatizer.lemmatize(token_corr, get_wordnet_pos(pos))
			lemmatized.append(lemm)
	return lemmatized
wor = ['I', 'apple', 'young']
print(lemmatize(wor))