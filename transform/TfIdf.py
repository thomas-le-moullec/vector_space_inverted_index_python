from transform.Transform import Transform


class TfIdf(Transform):

    def __init__(self):
        Transform.__init__(self)

    def tfidf_report(self, doc_id, key_words, nbr_unique, magnitude, similarity_score):
        print(doc_id)
