import nltk
import re
nltk.data.path.append('nltk_data')
from nltk.corpus import wordnet
# from nltk.tokenize import word_tokenize


class AntonymReplacer(object):
    def replace(self, word):
        antonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
        if len(antonyms) >= 1:
            return antonyms.pop()
        else:
            return None

    def cleantext(self, text):
        text = text.lower()
        text = re.sub(r"i'm", "i am", text)
        text = re.sub(r"he's", "he is", text)
        text = re.sub(r"she's", "she is", text)
        text = re.sub(r"that's", "that is", text)
        text = re.sub(r"what's", "what is", text)
        text = re.sub(r"where's", "where is", text)
        text = re.sub(r"what's", "what is", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"n't", "not", text)
        return text

    
    def negreplace(self, string):
        i = 0
        # sentence = word_tokenize(string)
        sentence = string.split(' ')
        len_sent = len(sentence)
        neg_sentence = ""
        while i < len_sent:
            word = sentence[i]
            if word == 'not' and i+1 < len_sent:
                ant = self.replace(sentence[i+1])
                if ant:
                    neg_sentence += ant+" "
                    i += 2
                    continue
            neg_sentence += word+" "
            i += 1
        neg_sentence = neg_sentence.strip()
        return neg_sentence


if __name__ == "__main__":
    replacer = AntonymReplacer()
    text = "I do n't love c++"
    clean_text = replacer.cleantext(text)
    sentence = replacer.negreplace(clean_text)
    print(sentence)
