# tf-idf: Term Frequency Inverse Document Frequency places more weight on occurences of infrequent words compared to common words

# Steps of tf-idf algo:
	# 1) Calc frequency(number of occurences divided by document length) for each word in collection of documents,
	# this is "term frequency"(tf), ignore capitalization and punctuation
	# 2) Calc how documents each word appears in, and divide this by total num of documents, this is "document frequency"(df)
	# Since we assign less weight to common words, we'll use idf = 1/df
	# 3) Most common way to combine 1) and 2); most common way:
	# tf-idf = tf x log(1/df)

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = [] # stores list of 8 values
        for word in vocabulary: # loops over each "unique" word
            result = tf[word][doc_index] *  math.log(1/df[word], 10) # calculates the tf-idf value
            tfidf.append(result) # appends to the list
        print(tfidf) # prints out the list

main(text)



