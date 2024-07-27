import os
import pickle

# function to map each term present in the corpus with the corresponding documentId
def term_document_mapping():
    directory_path = 'preprocessed_files'
    file_list = os.listdir(directory_path)
    term_docId = []

    for filename in file_list:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        
        content_list = content.split()
        for tkn in content_list:
            term_docId.append([tkn, filename])
    
    return term_docId
 
# function to sort the term-dcumentId list based on lexicographical order of term
def sorted_term_document(term_docid):
    # lambda sorted to the list of lists on the basis of first element
    sorted_term_docid = sorted(term_docid, key=lambda x: x[0])
    return sorted_term_docid

# functtion to create posting list for each term
def posting_list_mapping(term_docid):
    posting_list = {}
    for term in term_docid:
        token = term[0]
        document_id = term[1]
        if token not in posting_list:
            posting_list[token] = []
        if document_id not in posting_list[token]:
            posting_list[token].append(document_id)
    
    return posting_list


def map_terms_postings(posting_list):
    inverted_index = []
    for term in posting_list:
         # storng the posting list of term in a list
        postings = posting_list.get(term)
        
        # document frequency of a term t = number of documents in which t appears (or length of posting list)
        document_frequency = len(postings)
        
        # storing the term and document frequency in a dictionary
        term_info = {term : document_frequency}
        
        # combining the dictionary and list together 
        inverted_index.append([term_info, postings])
    return inverted_index
        


# step 1: Sequence of (Modified token, document ID) pairs 
term_docid = term_document_mapping()
        
# Step 2 : 
# Sorting the pairs in lexicographical order
sorted_term_docid = sorted_term_document(term_docid)

# step 3: 
# Map [{term, document frequency} -> {posting lists}]
# Remove duplicate and frequency information is added
# creating posting for every terms 
postings_list = posting_list_mapping(sorted_term_docid) 

# final step mapping each term with their corresponding postings list and document frequency
inverted_index = map_terms_postings(postings_list)

with open('boolean_inverted_index', 'wb') as file:
    pickle.dump(inverted_index, file)
