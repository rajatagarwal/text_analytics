"""
Part(a)
Load the file in and use nltk.word_tokenizer() on it. 
Report the list of tokens that are produced from it and note any oddities that arise. 
Comment on these oddities and how they might be handled.

Part(b)
Now, do normalization on it, and report this output as your answer.

Part(c)
Now, take the output from normalization step and run it through a pos-tagger. 
Report this output as your answer and highlight any inaccuracies that occur at this stage.
"""

#Part A
import nltk
targetFile = open('/Users/XXXX/dummyText1.txt')
rawtext    = targetFile.read()
print("Text file data: ")
print("============================================================================================================")
print(rawtext)

tokens = nltk.word_tokenize(rawtext)
print("")
print("Tokenised data: ")
print("============================================================================================================")
print(tokens)

#Part B
words = [w.lower() for w in tokens]
print("")
print("Normalised(lower case) data: ")
print("============================================================================================================")
print(words)

#Part C
pos_text = nltk.pos_tag(words)
print("")
print("POS Tagging data: ")
print("============================================================================================================")
print(pos_text)