from math import log2
from transform.Transform import Transform


class TfIdf(Transform):

    def __init__(self):
        Transform.__init__(self)

    def rank(self, term_freq, term_freq_max, doc_freq, nbr_docs):
        weight = term_freq / term_freq_max * log2(nbr_docs / doc_freq)
        return weight

    def get_weight(self, word, doc, index, documents):
        # Need to add the duplicate value
        term_frequency = doc.vocabulary[word] / sum(doc.vocabulary.values())
        max_term_frequency_key, max_term_frequency_value = doc.vocabulary.most_common(1)[0]
        max_term_frequency_value = max_term_frequency_value / sum(doc.vocabulary.values())
        doc_frequency = len(index[word])
        doc_nbr = len(documents)
        score = self.rank(term_frequency, max_term_frequency_value, doc_frequency, doc_nbr)
        return score
