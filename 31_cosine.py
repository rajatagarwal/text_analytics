# https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/

# Data Source: https://www.facebook.com/about/privacy (Facebook's privacy policy)
import math
from math import*
from collections import Counter
import matplotlib.pyplot as plt, numpy as np



# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

# Dictionary that will hold Tf-Idf metrics
vector_dict = {}

# Just load in all the documents
def load_docs():
	doc1 = ("d1", "Things you do and information you provide")
	doc2 = ("d2", "People you share information and communicate with")
	doc3 = ("d3", "Things others do and information they provide")
	return [doc1, doc2, doc3]

# Computes TF for words in each doc, DF for all features in all docs; finally whole Tf-IDF matrix 
def process_docs(all_docs):
	stop_words = [ 'of', 'and', 'on','in', 'from', 'that' ]
	all_words = []											# List to collect all the unique words in the documents
	counts_dict = {}										# dict to collect doc data, word-counts and word-lists
	for doc in all_docs:
		words = [x.lower() for x in doc[1].split() if x not in stop_words]
		words_counted = Counter(words)                      #counts words in a doc
		unique_words = list(words_counted.keys())           #list of the unique words in the doc
		counts_dict[doc[0]] = words_counted                 #make dict entry {'d1' : {'a': 1, 'b':6}}
		all_words = all_words + unique_words                #collect all unique words from each doc; bit hacky
	n = len(counts_dict)                                   	#number of documents is no of entries in dict
	df_counts = Counter(all_words)                          #DF of all unique words from each doc, counted
	compute_vector_len(counts_dict, n, df_counts)          #computes TF-IDF for all words in all docs

# Computes TF-IDF for all words in all docs
def compute_vector_len(doc_dict, no, df_counts):
	global vector_dict
	for doc_name in doc_dict:
		doc_words = doc_dict[doc_name].keys()                #get all the unique words in the doc
		wd_tfidf_scores = {}
		for wd in list(set(doc_words)):
			wds_cts = doc_dict[doc_name]                     #get the word-counts-dict for the doc
			wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)   #compute TF-IDF
			wd_tfidf_scores[wd] = round(wd_tf_idf, 4)        #store Tf-IDf scores with word
		vector_dict[doc_name] = wd_tfidf_scores              #store all Tf-IDf scores for words with doc_name
"""
def get_cosine(text1, text2):
	vec1 = vector_dict[text1]
	vec2 = vector_dict[text2]
	intersection = set(vec1.keys()) & set(vec2.keys())
	#NB strictly, this is not really correct, needs vector of all features with zeros
	numerator = sum([vec1[x] * vec2[x] for x in intersection])
	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)
	if not denominator:
		return 0.0
	else:
		return round(float(numerator) / denominator, 3)
"""

def square_rooted(x):
	return round(sqrt(sum([a*a for a in x])),3)
"""
def get_cosine(text1, text2):
	vec1 = vector_dict[text1]
	vec2 = vector_dict[text2]
	list1 = vec1.values()
	list2 = vec2.values()
	numerator = sum(a*b for a,b in zip(list1,list2))
	denominator = square_rooted(list1)*square_rooted(list2)
	return round(numerator/float(denominator),3)
"""


def get_euclidean_distance(text1, text2):
	vec1 = vector_dict[text1]
	vec2 = vector_dict[text2]
	list1 = vec1.values()
	list2 = vec2.values()
	return round(sqrt(sum(pow(a-b,2) for a, b in zip(list1, list2))), 3)

# Run
all_docs = load_docs()
process_docs(all_docs)
vector_dict['q'] = {'information' : 1, 'you' : 1, 'provide' : 1}

#for keys,values in vector_dict.items(): print(keys, values)

cosine_list = []
text2 = 'q'
# Cosine
for item in range(1,4):
	text1 = 'd' + str(item)
	cosine = get_cosine(text1, text2)
	cosine_list.append(cosine)
	#cosine_dict[text1] = cosine

cosine_list.append(1)
print(cosine_list)

# euclidean_distance
euclidean_distance_list = []

for item in range(1,4):
	text1 = 'd' + str(item)
	euclidean_distance = get_euclidean_distance(text1, text2)
	euclidean_distance_list.append(euclidean_distance)

euclidean_distance_list.append(1)
print(euclidean_distance_list)

#plot chart

jet=plt.get_cmap('jet')
x = [1,2,3, 4]
y1 = cosine_list
plt.title("Cosine Chart")
plt.xlabel("Documents")
plt.ylabel("Cosine Similarity Score")

p1 = plt.scatter(x,y1,marker="8", s=100, cmap=jet, color=['red'])

plt.text(1, cosine_list[0] + 0.02, "d1: " + str(cosine_list[0]))
plt.text(2, cosine_list[1] + 0.02, "d2: " + str(cosine_list[1]))
plt.text(3, cosine_list[2] + 0.02, "d3: " + str(cosine_list[2]))
plt.text(4, cosine_list[3] + 0.02, "Q: " + str(cosine_list[3]))

#plt.legend((p1, p2, p3, p4, p5),
#           ('S1 Normal - S1 Spam', 'S2 Normal - S1 Spam', 'S3 Normal - S1 Spam', 'S4 Normal - S1 Spam', 'S5 Normal - S1 Spam'),
#           scatterpoints=1,
#           loc='top right',
#           ncol=3,
#           fontsize=10)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()








