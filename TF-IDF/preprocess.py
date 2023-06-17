import os
import re

Qdata_ = "Leetcode_Scrapper/Qdata"

inval = "Example 1:"

all_lines = []

for i in range(1, 1403):
    file_path = os.path.join(Qdata_, "{}/{}.txt".format(i, i))

    doc = ""
    with open(file_path, "r", encoding= 'utf-8', errors = "ignore") as f:
        lines = f.readlines()
    
    for line in lines:
        if inval in line:
            break
        else:
            doc += line
    
    all_lines.append(doc)


def preprocess(text):      # remove problem no, and return a list of lowercase words
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)      # removing non alphanumeric chars
    terms = [term.lower() for term in text.strip().split()]

    return terms

vocab = {}          # word : no of docs that word is present in
documents = []      # all lists, with each list containing words of a document

for (index, line)  in enumerate(all_lines):
    tokens = preprocess(line)       #list of processed words of this doc
    documents.append(tokens)

    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

#reverse sort vocab by values (by the no of docs the word is present in)
vocab = dict( sorted(vocab.items(), key = lambda item : item[1], reverse = True) )



# keys of vocab thus is a set of distinct words across all docs
# save them in file vocab
with open("TF-IDF/vocab.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save idf values
with open("TF-IDF/idf-values.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])


#save the documents(lists of words for each doc)
with open("TF-IDF/document.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for doc in documents:
        f.write("%s\n" % doc)

inverted_index = {}         # word : list of index of docs the word is present in.
                    # inserting word multiple times from same doc too, so that we even get the term freq from here itself
for (index, doc) in enumerate(documents, start = 1):
    for token in doc:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)


# save the inverted index in a file
with open("TF-IDF/inverted_index.txt", 'w', encoding = 'utf-8', errors = "ignore") as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        
        doc_indexes = ' '.join([str(term) for term in inverted_index[key]])
        f.write("%s\n" % doc_indexes)