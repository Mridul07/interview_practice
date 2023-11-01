# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

def encode(list_of_strings):
    print(list_of_strings)

    encoded_string = ""
    for string in list_of_strings:
        encoded_string += str(len(string)) + "#" + string 

    print(encoded_string)
    return encoded_string

def decode(encoded_input):
    res, i = [], 0

    while i < len(encoded_input):
        j = i
        while encoded_input[j] != "#":
            j += 1
        curr_len = int(encoded_input[i:j])
        res.append(encoded_input[j+1:j+1+curr_len])
        i = j+1+curr_len

    return res


list_of_strings = ["Hello","ho#w","are","you","doing"]
encoded_input = encode(list_of_strings)

decoded_list = decode(encoded_input)

if decoded_list == list_of_strings:
    print("Passed")
else:
    print("Failed")
