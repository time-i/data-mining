import nltk.downloader
import nltk
from nltk.corpus import brown
nltk.download('punkt')
text = "The quick brown fox jumped over the lazy dog"
words = brown.words(text)
print(words)