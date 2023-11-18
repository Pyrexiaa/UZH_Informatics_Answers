from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):

    indexed_dict = {}
    for index, string in enumerate(dataset):
        indexed_dict[index] = string
    
    index_dictionary = {}
    for key, value in indexed_dict.items():
        items = value.split(" ")
        for item in items:
            item = item.lower()
            if item not in index_dictionary:
                index_dictionary[item] = [key]
            else:
                index_dictionary[item].append(key)
    # don't forget to return your resulting dictionary
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
