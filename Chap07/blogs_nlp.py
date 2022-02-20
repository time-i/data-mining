
from nltk.tokenize import word_tokenize

# pos tagging
from nltk import pos_tag
tokens = word_tokenize("Hello! I'am Nancy.")
pos_tags = pos_tag(tokens)
print(pos_tags)

# stemming

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stems = stemmer.stem('fishes')
print(stems)
stems = stemmer.stem('fishing')
print(stems)

# lemma

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemma = lemmatizer.lemmatize('go', pos='v')
print(lemma)
lemma = lemmatizer.lemmatize('went')
print(lemma)
lemma = lemmatizer.lemmatize('went', pos='v')
print(lemma)

# stopword

from nltk.corpus import stopwords
stop_list = stopwords.words('english')
print(len(stop_list))
print(stop_list[:10])

# synonym

synonyms = {'big': 'large', 'purchase': 'buy'}
text = "I want to purchase a book on Big Data".lower().split()
print(text)
new_text = [synonyms.get(word, word) for word in text]
print(new_text)

from nltk.corpus import wordnet
syns = wordnet.synsets('big', pos='a')
for syn in syns:
    print(syn.lemma_names())