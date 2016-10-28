import nltk

pos_phrases = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

phrases = []
words_filtered = []
for(words, sentiment) in pos_phrases + neg_phrases:
	for(e in words.split()):
			if(len(e) >= 3):
				words_filtered.extend(e.lower())
phrases.append(words_filtered, sentiment)

def get_words(phrase):
	all_words = []
	for(words, sentiment) in phrase:
		all_words.extend(words);
	return all_words

print get_words("my day was okay")