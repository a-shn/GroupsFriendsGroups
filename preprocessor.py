import string
import re
import api_handler
import lemmatizer_eng, stemmer_rus

def has_cyrillic(text):
	return bool(re.search('[а-яА-Я]', text))


def has_english(text):
	return bool(re.search('[a-zA-Z]', text))

def remove_word_trash(word):
	res = ''
	for char in word:
		if str.isalpha(char):
			res += char
	return res

def remove_punctuation(filename):
	try:
		with open(filename, 'r') as infile:
			text = infile.read()
			for p in string.punctuation:
				text = text.replace(p, ' ')
			infile.close()
		with open(filename, 'w') as outfile:
			outfile.write(text)
			outfile.close()
	except:
		print('Error')

def lemmatize(filename):
	russian = []
	english = []
	try:
		with open(filename, 'r') as infile:
			text = infile.read().split(' ')
			for word in text:
				if has_cyrillic(word):
					russian.append(remove_word_trash(word))
				elif has_english(word):
					english.append(remove_word_trash(word))
			infile.close()
		russian = stemmer_rus.lemmatize(russian)
		english = lemmatizer_eng.lemmatize(english)
		with open(filename, 'w') as new:
			new.close()
		with open(filename, 'a') as outfile:
			for word in russian:
				outfile.write(word + ' ')
			for word in english:
				outfile.write(word + ' ')
			outfile.close()
	except:
		print('Error')

# lemmatize('76189507' + '_TEXT.txt')

for friend in api_handler.get_friends(76189507):
	lemmatize(str(friend) + '_TEXT.txt')

