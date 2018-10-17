import re
import string


class Parser:
    def __init__(self):
        self.mini_len_word = 4

    @staticmethod
    def __remove_punctuation(string_name):
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        new_string = string_name.translate(translator)
        return new_string

    @staticmethod
    def __remove_small_words(words):
        short_words = re.compile(r'\W*\b\w{1,3}\b')
        words_parsed = short_words.sub('', words)
        return words_parsed

    # Function to parse a document. This is basically called by a query(which is a document) and a random document
    def parse_doc(self, document):
        # Normalize : Remove every punctuation and small words (less than 4 characters). We also put in lower case
        # Extension possible : Could remove the stop_words
        words = self.__remove_punctuation(document)
        words = self.__remove_small_words(words)
        words = words.lower()
        # Tokenize : interpret each whitespace as a word separator
        words = words.split()
        return words

    @staticmethod
    def parse_term(term):
        if term[-1] == 's':
            term = term[:-1]
        return term

    @staticmethod
    def remove_stop_words(document):
        pass

