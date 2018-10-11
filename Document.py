from collections import Counter


class Document:
    def __init__(self):
        self.vocabulary = Counter()
        self.vector = {}

    def get_unique_keywords_nbr(self):
        counter = 0
        vocabulary = self.vocabulary.most_common()[:-len(self.vocabulary)-1:-1]
        print(vocabulary)
        for term in vocabulary:
            if term[1] != 1:
                break
            counter += 1
        return counter
