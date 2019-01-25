# Vocabulary Wizard
A simple tool that uses the WordsAPI for user input words. I created this program to simplify a recurring assignment my son has for school. 

Currently this program:

    - Runs in a loop and allows user to quit gracefully
    - Takes user input
    - Prints, when available, the word's definition, synonyms, antonyms, and examples
    - Uses try/excepts to handle errors produced when one of these values do not exist
    
Please note that this program:

    - Requires you obtain your own API key on RapidAPI. Simply add the key to to .py in the area specified
    - Python3 is not supported by this program due to the use of the unirest module
    
Please feel free to contribute or provide feedback on how to improve this code. Specifically, I would like to look at the potential use of parameters in a single function, the use of list comprehensions, better error handling, perhaps creating a Class, and how to best refactor this code. 
