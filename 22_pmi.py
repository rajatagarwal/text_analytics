# Caclulate PMI Scores
#
#
# Definition
# Mutual Information (MI) and Pointwise Mutual Information (PMI): 
# use observed frequency of the pair and an expected frequency of the pair under the assumption that the parts are independent
#
#
# Formula
# log base 2 of probability of w1 and w2 over the probability of w1-alone by w2-alone
#
#                       P(w1, w2)
# PMI(w1, w2)  =  log2-------------
#	                   P(w1), P(w2)	
#
# for ease of computation, which can be translated to
#
#
# PMI(w1, w2)  =  log2(C(w1, w2)) + log2(N) - log2(C(w1)) - log2(C(w2))
#
#
# C() is a counting function; N is sample size, no. of items in corpus or list of pairs examined
#
# Requirements:
# There is nltk BigramAssocMeasures() package to help you out.
#
##############################################################################################################################################################

import nltk
from nltk.collocations import *

# Read raw text
target_file = open('Output_Full_lemmatize.txt')
rawtext = target_file.read()
bigram_pairs = list(nltk.bigrams(rawtext.split()))

# Bigram calculation for each pair
print("\n\n All pairs:")
print("====================================")
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(rawtext.split())
for item, pmi_score in finder.ngram_fd.items():
	print(item, pmi_score)

print("\n\n Top 10 Pairs(Doesn't make much sense):")
print("====================================")
# Bigram measurement to get top 10 word pairs
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(rawtext.split())
bigram_list = finder.nbest(bigram_measures.pmi, 10)

# Print each pair
for item in bigram_list:
	print(item)

# Apply filter
print("\n\n Top Pairs after applying fiter:")
print("====================================")
finder.apply_freq_filter(2)
for item, pmi_score in finder.ngram_fd.items():
	print(item, pmi_score)
