import nltk
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

    
    def negreplace(self, string):
        i = 0
        # sentence = word_tokenize(string)
        sentence = string.split(' ')
        print(sentence)
        len_sent = len(sentence)
        words = []
        while i < len_sent:
            word = sentence[i]
            if word == 'not' and i+1 < len_sent:
                ant = self.replace(sentence[i+1])
                print(ant)
                if ant:
                    words.append(ant)
                    i += 2
                    continue
            words.append(word)
            i += 1

        return words


if __name__ == "__main__":
    replacer = AntonymReplacer()
    sentence = replacer.negreplace('this is not good')
    print(sentence)
