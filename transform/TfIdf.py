from math import log2
from transform.Transform import Transform


class TfIdf(Transform):

    def __init__(self):
        Transform.__init__(self)

    def rank(self, term_freq, term_freq_max, doc_freq, nbr_docs):
        weight = term_freq / term_freq_max * log2(nbr_docs / doc_freq)
        return weight

    def tfidf_report(self, doc_id, key_words, nbr_unique, magnitude, similarity_score):
        print(doc_id)
