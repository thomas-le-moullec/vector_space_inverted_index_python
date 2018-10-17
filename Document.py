from collections import Counter
from math import sqrt


class Document:
    def __init__(self):
        self.vocabulary = Counter()
        self.vector = {}

    # Get the magnitude L2 of the weights vector. This is useful to compute the cosine similarity
    def get_magnitude(self):
        norm = 0
        for term in self.vector:
            norm += self.vector[term] * self.vector[term]
        return sqrt(norm)

    # Function to get the number of unique keywords in the document
    # Actually I decided to consider Unique term as 'Distinct'
    def get_unique_keywords_nbr(self, index, doc_id):
        # Unique:
        '''counter = 0
        vocabulary = self.vocabulary.most_common()[:-len(self.vocabulary)-1:-1]
                for term in vocabulary:
                    if term[1] != 1:
                        break
                    counter += 1 '''
        # Distinct
        counter = len(self.vocabulary)
        return counter
