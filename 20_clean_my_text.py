# This will read a text file, normalize it and remove stopwords from it using nltk.
import nltk, io, math
from nltk.corpus import stopwords
from string import punctuation

# Read raw text
targetFile = open('input_text.txt')
rawtext = targetFile.read()

# Remove punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)
filtered_punc = strip_punctuation(rawtext)

# Removing stopwords
stops = set(stopwords.words('english'))
filtered_text = [i for i in filtered_punc.lower().split() if i not in stops]

# Lemmatization
wnl = nltk.WordNetLemmatizer()
lemmatized_words = [wnl.lemmatize(text) for text in filtered_text]

# Count Number of words
total_words = len(lemmatized_words)

# Divide them equally into 10 different lists
chunk_size = math.floor(total_words/10)
n_lists_of_words = [filtered_text[i:i + chunk_size] for i in range(0, len(filtered_text), chunk_size)]
if(len(n_lists_of_words) > 10):
	del n_lists_of_words[-1]

# Lets make list of strings instead of list of lists
list_of_str = [' '.join(x) for x in n_lists_of_words]

# Print list values in seperate files
for index, sentence in enumerate(list_of_str):
	with open("tfidf/Output_lemmatize_" + str(index) + ".txt", "w") as text_file:
		print(sentence, file=text_file)

# Print full text in a seperate  file for further use
full_text = ' '.join(list_of_str)
with open("Output_Full_lemmatize.txt", "w") as text_file:
	print(full_text, file=text_file)
