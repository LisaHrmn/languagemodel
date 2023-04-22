import random

text = "winnie_the_pooh.txt"

# n is amount of words n-grams to look at (1=unigram, 2=bigram, 3=trigram)
n = 4

# a is amount of words will generate
a = 30

with open(text) as t:
    contents = t.read()

# make the text all lower cased
contents = contents.lower()

# remove punctuation 
# punctuations = string.punctuation
punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
contents = contents.translate(str.maketrans('', '', punctuations))
contents = contents.replace('.', ' .')
#print(contents.split())

def get_ngrams(text, n):
    # tokenize (split up the text in smaller parts)
    tokens = text.split()
    ngrams = []

    # get those ngrams
    for i in range(len(tokens)-n+1):
       temp=[tokens[j] for j in range(i,i+n)]
       ngrams.append(" ".join(temp))
    
    return ngrams

ngrams = get_ngrams(contents, n)
#print(ngrams) 

# # get dict of amount of times each ngram appears 
# def ngrams_freqs(ngrams):
#     count = {}
#     for ngrams in ngramlist:
#         # if ngram doesnt exist yet create count
#         if ngrams not in count:
#             count[ngrams] = 1
#         # if ngram already exists addd one
#         else:
#             count[ngrams] += 1
#     return count

# ngram_freqs = ngrams_freqs(ngrams)
# # print(ngram_freqs)

# need to figure out most likely next word to previous word 
# get dict of all associated words to word
def asso_dict(ngrams):
    asso_dict = {}
    prev_word = ''
    for words in ngrams:
         if prev_word not in asso_dict:
             asso_dict[prev_word] = []
         asso_dict[prev_word].append(words)
         prev_word = words
    return asso_dict

asso_dict = asso_dict(ngrams)
#print(asso_dict)

# get a random start word/phrase
# generate sentences 
def generatetext(a):
    words = []
    next_word = random.choice(list(asso_dict.keys()))
    words.append(next_word)
    # now next random choice of words that could come after given word
    while len(words) < a:
        next_word = random.choice(asso_dict[next_word])
        # if we use n > 1 remove duplicate ngrams
        splitword = next_word.split()
        words.append(splitword[-1])
    
    return ' '.join(words)

print(generatetext(a))