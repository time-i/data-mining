import nltk
nltk.download('averaged_perceptron_tagger')
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from string import punctuation
#
# text = 'Compatibility of systems of linear constraints over the set of natural numbers.'
# # 分词
# words_before = word_tokenize(text.lower())
#
# # 删除停用词和标点符号
# stopwords = set(stopwords.words('english') + list(punctuation))
#
# words = []
# for w in words_before:
#     if w not in stopwords:
#         words.append(w)
#
# # 词性标注
# pos_tags = nltk.pos_tag(words)
# print(pos_tags)
