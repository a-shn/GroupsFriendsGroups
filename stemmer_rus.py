import nltk

nltk.download("stopwords")
# --------#

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

mystem = Mystem()
russian_stopwords = stopwords.words("russian")


def preprocess_text(text):
	tokens = mystem.lemmatize(text.lower())
	tokens = [token for token in tokens if token not in russian_stopwords \
	          and token != " " \
	          and token.strip() not in punctuation]

	text = " ".join(tokens)

	return text


def lemmatize(words):
	stemmed = []
	for word in words:
		if preprocess_text(word) != '':
			stemmed.append(preprocess_text(word))
	return stemmed
