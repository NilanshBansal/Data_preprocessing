import re,string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = stopwords.words('english')
newStopWords = ['RT','Re']
stop_words.extend(newStopWords)
stop_words=set(stop_words)

def elim_stopwords(sentence):
    tokens = word_tokenize(sentence)
    
    i_offset = 0
    for i, t in enumerate(tokens):
        i -= i_offset
        if (t == '#' or t.startswith("'")) and i > 0:
            left = tokens[:i-1]
            joined = [tokens[i - 1] + t]
            right = tokens[i + 1:]
            tokens = left + joined + right
            i_offset += 1

    # filtered_sentence = [w for w in tokens if not w in stop_words] 
    filtered_sentence = [w for w in tokens if not w in ['RT','Re']] 
    filtered_sentence = ' '.join(filtered_sentence)
    return filtered_sentence

def strip_links(text):
    link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#',"'","+","?"]
    for separator in string.punctuation:
        if separator not in entity_prefixes:
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

# Cleansing Data -> Removing @, #, RT, Re, links, Html data

tests = [
    "I am at Starbucks http://4sh.com/samqUI (7419 3rd ave, at 75th, Brooklyn)",
    "I c RT @iamFink: @SamanthaSpice that's my excited face and my regular face. The expression never changes.",
    "RT @AstrologyForYou: #Gemini recharges through regular contact with people of like mind, and social involvement that allows expression of their ideas",
    "New comment by diego.bosca: Re: Re: wrong regular expression? http://t.co/4KOb94ua",
    
    "@lakatos88 Python framework wasn't good.",
    "@peter I really love that shirt at #Macy. http://bet.ly//WjdiW4",
    "I love C++",
    "I love C#",
    "Do I love C#?",
]

# tests = [
#     "RT @iamFink: @SamanthaSpice that's my excited face.",
#     "@lakatos88 Python framework wasn't good.",
# ]


for t in tests:
    print(elim_stopwords(strip_all_entities(strip_links(t))))
    # print(strip_all_entities(strip_links(t)))