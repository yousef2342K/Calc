def check_key(dictionary, key):
    if key in dictionary:
        print("Key '{}' exists in the dictionary.".format(key))
    else:
        print("Key '{}' does not exist in the dictionary.".format(key))


# Example
my_dict = {"apple": 1, "banana": 2, "orange": 3}

check_key(my_dict, "apple")  # Key 'apple' exists in the dictionary.
check_key(my_dict, "grape")  # Key 'grape' does not exist in the dictionary
