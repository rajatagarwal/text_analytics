"""
Stemming & Lemmatisation

Part(a)
Tokenize a new text-file (200 words) and the stem it using Porter Stemming. Report your answer and some of weird things that Porter Stemming does.

Part(b)
Tokenize the new text-file and then lemmatize it using WordNet Lemmatizer; 
note you may have to pos-tag the sentences first and then convert the tags to make this work. 
Report the result of these steps and point out some of the things that look wrong.

Part(c)
Compare the outputs from Porter Stemming and the Lemmatisation of the same file. Which do you think is the best to use and why?
"""

#Part(a)
import nltk
from nltk.stem import WordNetLemmatizer

targetfile = open("/Users/RajatAgarwal/Desktop/TA Assignment/Lab 1/dummyText2.txt")
rawtext = targetfile.read()
print("Text file data: ")
print("============================================================================================================")
print(rawtext)

tokens = nltk.word_tokenize(rawtext)
words = [w.lower() for w in tokens]

stemmer = nltk.PorterStemmer()
stemmed_output = [stemmer.stem(wd) for wd in words]
print("")
print("Stemmed data: ")
print("============================================================================================================")
print(' '.join(stemmed_output))

#Part(b)
words = [w.lower() for w in tokens]
#Pos
pos_text = nltk.pos_tag(words)

def get_lemmatize(pos):
	wnl = WordNetLemmatizer()
	for word, tag in pos:
		if tag.startswith("NN"):
			yield wnl.lemmatize(word, pos="n")
		elif tag.startswith("VB"):
			yield wnl.lemmatize(word, pos="v")
		elif tag.startswith("JJ"):
			yield wnl.lemmatize(word, pos="a")
		else:
			yield word
print("Lemmatized data: ")
print("============================================================================================================")
print(' '.join(get_lemmatize(pos_text)))








