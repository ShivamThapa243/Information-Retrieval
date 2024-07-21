# function to convert into lowercase
def lowercase_processing(to_lowercase):
    return to_lowercase.lower()

# function to convert string into tokens
def token_processing(to_token):
    tokens = to_token.split()
    return tokens

# function to remove stopwords form tokens
def stopword_processing(tokens):
    stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                 "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
                 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
                 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
                 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
                 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
                 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
                 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
                 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
                 "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
                 "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"}
    new_tokens = []
    for tkn in tokens:
        if tkn in stopwords:
            continue
        else:
            new_tokens.append(tkn)
    return new_tokens

# function to remove punctuation marks
def punctuation_processing(tokens):
    new_tokens = []
    # list of punctuation marks
    punctuation_list = ['.', '?', '!', ',', ';', ':', '\'', '\"', '-', '_', ')', '(', '[', ']', '{', '}', '<', '>', '='
                        , '/', '\\', '*', '#']
    # iterating though every string inside the tokens list
    for token in tokens:
        temp = ""
        # checking if the character matches the punctuation list
        for tkn in token:
            if tkn in punctuation_list:
                continue                    # if it matches do nothing
            else:
                temp += tkn                 # else add the character in the temp variable
        # end of inner for-loop

        new_tokens.append(temp)
    # end of outer for-loop
    return new_tokens

# function to convert list to string
def to_string(token_list):
    token_string = ""
    for token in token_list:
        token_string += token 
        token_string += " "
    return token_string

# Preprocessing Function
def preprocessing_file(content):

    # converting strings into lowercase
    lowercase_content = lowercase_processing(content)

    # converting strings into tokens
    tokens = token_processing(lowercase_content)

    # updated tokens after removing stopwords
    tokens_without_stopwords = stopword_processing(tokens)

    # removing punctuations "." , "," , "-" , ":", ";"
    tokens_without_punctuation = punctuation_processing(tokens_without_stopwords)

    preprocessed_tokens = to_string(tokens_without_punctuation)

    return preprocessed_tokens