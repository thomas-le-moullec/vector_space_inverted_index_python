from math import sqrt

from similarity.Similarity import Similarity


class Cosine(Similarity):

    def __init__(self):
        Similarity.__init__(self)

    @staticmethod
    def __get_inner_product(doc_vector, query_vector):
        inner_product = 0
        for query_term in query_vector:
            if query_term in doc_vector:
                inner_product += (doc_vector[query_term] * query_vector[query_term])
        return inner_product

    def __cos(self, doc, query, idx):
        inner_product = self.__get_inner_product(doc.vector, query.vector)
        norm_doc = doc.get_magnitude()
        norm_query = sqrt(len(query.vector))
        similarity = 0
        if norm_query != 0 and norm_doc != 0:
            similarity = inner_product / (norm_doc * norm_query)
        return similarity

    def get_similarity(self, doc_vector, query_vector, idx):
        return self.__cos(doc_vector, query_vector, idx)
