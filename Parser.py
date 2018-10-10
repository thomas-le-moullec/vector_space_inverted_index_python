import re
import string


class Parser:
    def __init__(self):
        self.mini_len_word = 4

    def __remove_punctuation(self, string_name):
        translator = str.maketrans('', '', string.punctuation)
        new_string = string_name.translate(translator)
        return new_string

    def __remove_small_words(self, words):
        short_words = re.compile(r'\W*\b\w{1,3}\b')
        words_parsed = short_words.sub('', words)
        return words_parsed

    def parse_doc(self, document):
        words = self.__remove_punctuation(document)
        words = self.__remove_small_words(words)
        print("In parse_doc: ")
        print(words)
        words = words.split()
        return words

    def parse_term(self, term):
        return True

    def remove_stop_words(self, document):
        pass

