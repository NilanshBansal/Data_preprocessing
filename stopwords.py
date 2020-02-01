from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example_sent) 

filtered_sentence = [w for w in word_tokens if not w in stop_words] 

print(word_tokens) 
print(filtered_sentence) 

filtered_sentence = ' '.join(filtered_sentence)

print(filtered_sentence)


# stopwords = nltk.corpus.stopwords.words('english')
# newStopWords = ['stopWord1','stopWord2']
# stopwords.extend(newStopWords)