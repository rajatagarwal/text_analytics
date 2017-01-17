import math, nltk
from string import punctuation

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)

# Regular set
targetFile = open('tweets/regular_set.txt')
regulartext = targetFile.read()
regulartext = regulartext.lower()
regulartext = strip_punctuation(regulartext)
regulartext = list(regulartext)
print("REGULAR TWEETS ENTROPY:")
print("==================================")
print(entropy(regulartext))

# Spam set
targetFile = open('tweets/spam_set.txt')
spamtext = targetFile.read()
spamtext = spamtext.lower()
spamtext = strip_punctuation(spamtext)
spamtext = list(spamtext)
print("\n\nSPAM TWEETS ENTROPY:")
print("==================================")
print(entropy(spamtext))

# Spam set
targetFile = open('tweets/mixed_set.txt')
mixedtext = targetFile.read()
mixedtext = mixedtext.lower()
mixedtext = strip_punctuation(mixedtext)
mixedtext = list(mixedtext)
print("\n\nMIXED TWEETS ENTROPY:")
print("==================================")
print(entropy(mixedtext))