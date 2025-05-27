# -*- coding: utf-8 -*-

"""
# This project will be a text-formatter that will generate tables.
# The provided insights: The prevalence of a word in a set
# The features: Toggle case sensitivity, print or save as csv, and others
"""
# %%
from tabulate import tabulate
import string

# %%
# --- FUNCTION DEFINITIONS (MOVED TO TOP LEVEL) ---


def countingwords(word_list):
    """ Function for logging word usage.

    Args: word_list.

    Return:
        dict: A dictionary where keys are words and values are their counts.
        """
    word_counts = {}  # Empty dictionary

    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    for word in word_list:  # Process each word
        # Remove punctuation first
        cleaned_word = word.translate(translator)

        # Convert to lowercase for case-insensitivity
        widenetcase = cleaned_word.lower()

        # Only count if the word is not empty after cleaning
        if widenetcase:  # Checks if the string is not empty
            if widenetcase in word_counts:
                word_counts[widenetcase] += 1  # COUNTS WORD
            else:
                word_counts[widenetcase] = 1  # 1 = new addition
    return word_counts


def displaytable(word_counts):
    sorted_word_counts = sorted(
        word_counts.items(), key=lambda item: item[1])
    table_data = []
    for word, count in sorted_word_counts:
        table_data.append([word, count])
    headers = ["Words", "Usage"]
    print(tabulate(table_data, headers=headers,
                   tablefmt="pretty", numalign="right", stralign="left"))

# --- END FUNCTION DEFINITIONS ---


print("oo--***-----***-----***----***----***---oo")
print(" " + "Welcome  to  Data  Formatter!" + " ")
print("...++--**--++--**--++--**--++.....")
print("My functionality is limited..")
print(" but feel free to copy and paste the results!")
print(". .. ...++--**--++--**--++--**--++--**--... .. .")

# Yes or no prompt
binaryinput = input(
    "Did you want to gain insight on your text? Y/N or ? : ")
# %%
if binaryinput.lower() == "no" or binaryinput.lower() == "n":
    print("o---o---o" + "I understand" + "o---o---o--o")
    print("...._...._._..._.Goodbye!.._..._._....._.")
    exit()
elif binaryinput.lower() == "?" or binaryinput.lower() == "help":
    print("I am a text formatter!")
    print("--+---+--" + "Paste your text and press enter!" + "--+--+--+")
elif binaryinput.lower() == "y" or binaryinput.lower() == "yes":
    print(".._.._.._..._...._...._._....._.._.._...._.._..")
    print("Paste it, and I'll organize it!")
    promptfromuser = input("*-*-*" + "paste it here:  ")
    print("++.--**-.-+.+-.-*.*-.-+.+-.-**-.-+.+")
    word_list = promptfromuser.split(" ")  # word_list is defined here

    # functions are now defined globally
    word_counts = countingwords(word_list)
    displaytable(word_counts)             # and can be called here

else:
    print("++--**--++--**--++--**--++")
    print("Invalid! Please type 'yes', 'no', 'exit' or 'help'.")
    numbertwoprompt = input("Type your choice, here: ")
    if numbertwoprompt.lower() == "exit":
        print("..-.*.+--**-...*...Goodbye!.*..*...*..*..")
        exit()
    else:
        pass

print(".....*....*.....*....*....*....*....*.....*...*...*")
print("x----------x---------x------------x---------x------x")
