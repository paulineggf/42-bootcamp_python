import sys
import string

def print_result(upper_letter, lower_letter, punctuation_marks, spaces, characters):
    print ("The text contains", characters, "characters:")
    print ("- ", upper_letter, "upper letters")
    print ("- ", lower_letter, "lower letters")
    print ("- ", punctuation_marks, "punctuation marks")
    print ("- ", spaces, "spaces")

def text_analyzer(s = ""):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if len(s) == 0:
        print ("What is the text to analyse?")
        s = input()
    upper_letter = 0
    lower_letter = 0
    punctuation_marks = 0
    spaces = 0
    characters = 0
    for i in range(0, len(s)):
        if s[i].isupper():
            upper_letter += 1
        elif s[i].islower():
            lower_letter += 1
        elif s[i].isspace():
            spaces += 1
        elif s[i] in string.punctuation:
            punctuation_marks += 1
        characters += 1
    print_result(upper_letter, lower_letter, punctuation_marks, spaces, characters)
