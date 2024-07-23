import os
import pickle
import preprocessing

# function name to int and sorting
def to_numeric_sorted_list(str_list):
    int_list = []
    for num in str_list:
        int_list.append(int(num))
    int_list.sort()
    return int_list

#function difference
def difference(list1):
    corpous_list = []
    dir_path = "preprocessed_files"
    file_list = os.listdir(dir_path)
    
    for filename in file_list:
        corpous_list.append(filename)
    
    corpous_list = to_numeric_sorted_list(corpous_list)
    
    if(len(list1) == 0):
        return corpous_list
    else:
        for num_id in list1:
            if num_id in corpous_list:
                corpous_list.remove(num_id)
        return corpous_list
    
    
# function to return intersection of two lists
def intersect(list1, list2):
     
    intersect_list = []
    
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] == list2[0]:
            intersect_list.append(list2[0])
            list1.pop(0)
            list2.pop(0)
        elif list1[0] < list2[0]:
            list1.pop(0)
        else:
            list2.pop(0)
    return intersect_list

#function to return union
def union(list1, list2):
    union_list = []
    while(len(list1) > 0 and len(list2) > 0):
        if(list1[0] == list2[0]):
            union_list.append(list1[0])
            list1.pop(0)
            list2.pop(0)
        elif list1[0] < list2[0]:
            union_list.append(list1[0])
            list1.pop(0)
        else:
            union_list.append(list2[0])
            list2.pop(0)
    if len(list1) > 0:
        union_list += list1
    if(len(list2) > 0):
        union_list += list2
    return union_list

#function to perform operation on sequence tokens and operations
def operations_on_inverted_index(sequence_tokens, operations):
    operation_list = operations
    queue_posting = []
    
    for term in sequence_tokens:
        found = False
        for entry in inverted_index:
            term_dict = entry[0]
            if(term in term_dict):
                posting = entry[1]
                found = True
                break
        if not found:
            posting = []
        queue_posting.append(posting)

    while(len(operation_list) > 0 ):
        operator = operation_list.pop(0)
        
        if len(operation_list) == 0 and  operator.lower() == "not":
            first_list = queue_posting.pop(0)
            first_list = to_numeric_sorted_list(first_list)
            temp_list = difference(first_list)
        
        else:
            list1 = queue_posting.pop(0)
            list2 = queue_posting.pop(0)
            
            first_list = to_numeric_sorted_list(list1)
            second_list = to_numeric_sorted_list(list2)
            
                
            if operator.lower() == "and":
                temp_list = intersect(first_list, second_list)
                
            elif operator.lower() == "or":
                temp_list = union(first_list, second_list)
                
            elif operator.lower() == "and not":
                not_first_list1 = difference(list1)
                temp_list = intersect(not_first_list1, second_list)
            
            elif operator.lower() == "or not":
                not_first_list1 = difference(list1)
                temp_list = union(not_first_list1, second_list)        
        queue_posting.append(temp_list) 
    
    return queue_posting[0]

# Initial part (main)

print("Number of queries to execute")
n = input()
n = int(n)

while (n > 0): 
    with open('boolean_inverted_index', 'rb') as file:
        inverted_index = pickle.load(file) 

    print("Enter input sequence :")
    input_sequence = input()

    print("Enter operations : ")
    operations = input()
    operation_list = operations.split(", ")

    tokens_list = preprocessing.preprocessing_file(input_sequence)
    tokens_list = tokens_list.split()

    copy_operation_list = operation_list[:]

    queue_posting = operations_on_inverted_index(tokens_list, copy_operation_list) 

    query_retrieved = tokens_list[0]

    for i in range(len(operation_list)):
        query_retrieved += f" {operation_list[i]} {tokens_list[i+1]}"

    print(query_retrieved)

    print(queue_posting)
    
    n-=1
