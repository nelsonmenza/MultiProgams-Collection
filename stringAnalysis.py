# Program Name: String Analysis

import random

# Function to calculate the length of a string


def length(string):
    new_string = ""
    for i in string:
        if i != " ":
            new_string = new_string + i
    return len(new_string)

# Function to retrieve the character at the sixth position of a string


def sixth_position(string):
    if len(string) >= 6:
        return string[6]
    else:
        return "This string doesn't have more than 5 characters"

# Function to extract the last word(s) from a string


def last_word(string):
    list_word = []
    lastword = ""
    for i in string:
        if i == "," or i == ".":
            continue
        elif i != " ":
            lastword = lastword + i
        else:
            if lastword != "":
                list_word.append(lastword)
                lastword = ""
    if lastword != "":
        list_word.append(lastword)
    return list_word

# Function to count the occurrences of each word in a list and print the results


def word_count(word_list):
    word_dict = {}
    for key in word_list:
        if key in word_dict:
            word_dict[key] += 1
        else:
            word_dict[key] = 1
    for key, value in word_dict.items():
        print("{} : {}".format(key, value))


# Main program
string = input("Enter something: ")

# Calculate and print the number of characters in the string
print("The number of characters is: ", length(string))

# Retrieve and print the character at the 6th position of the string
print("The character in the 6th position is: ", sixth_position(string))

# Convert the string to uppercase and print the result
print("The string in uppercase is: ", string.upper())

# Extract the last word from the string and print it
word_list = last_word(string)
print("The last word is: ", word_list[-1])

# Repeat the last word a random number of times and print the result
repeated_word = f"{word_list[-1]} " * random.randint(1, 10)
print("The last word repeated a random number of times: ", repeated_word)

# Count the occurrences of each word and print the results
print("--------WORD COUNT--------")
word_count(word_list)
