from math import sqrt

from Document import Document
from Parser import Parser
from transform import TfIdf


class VectorSpace:

    def __init__(self, dictionnaries=[], transforms=TfIdf.TfIdf()):
        self.dictionnaries = dictionnaries
        self.transform = transforms
        self.doc_id = 0
        self.parser = Parser()
        self.index = {}
        self.documents = []

    def index_term(self, term, idx_term, idx_doc):
        if term[-1] == 's':
            term = term[:-1]
        if term not in self.index:
            self.index[term] = {}
        if idx_doc not in self.index[term]:
            self.index[term][idx_doc] = []
        self.index[term][idx_doc].append(idx_term)
        self.documents[idx_doc].vocabulary.update({term: 1})

    def index_document(self, document, idx_doc):
        words = self.parser.parse_doc(document)
        if not words:
            return False
        self.documents.append(Document())
        for idx_term, term in enumerate(words):
            self.index_term(term, idx_term, idx_doc)
        return True

    def __make_vectors_weight(self):
        for idx_doc, doc in enumerate(self.documents):
            # Construct the vector space for this document, associate a term with a weight
            self.__make_doc_vector(idx_doc)
            # Order the document vector space by highest weight
            self.documents[idx_doc].vector = [(k, self.documents[idx_doc].vector[k]) for k in sorted(self.documents[idx_doc].vector, key=self.documents[idx_doc].vector.get, reverse=True)]
            self.documents[idx_doc].vector = dict(self.documents[idx_doc].vector)

    def index_collection(self, docs_collection=[]):
        if docs_collection:
            self.dictionnaries = docs_collection
        elif not docs_collection and not self.dictionnaries:
            print("No collection to index. Please give a list of documents to index_collection function")
            return False
        for doc in self.dictionnaries:
            indexed = self.index_document(doc, self.doc_id)
            if indexed:
                self.doc_id += 1
        # Once the inverted index is completed, we calculate the vector space of weights thanks to the tfidf
        # (Or any other transform)
        self.__make_vectors_weight()
        return True

    def __make_doc_vector(self, idx_doc):
        for term in self.documents[idx_doc].vocabulary.keys():
            self.documents[idx_doc].vector[term] = self.transform.get_weight(term, self.documents[idx_doc],
                                                                             self.index, self.documents)

    def __make_query_vector(self, search, doc):
        query_vector = {}
        for word in search:
            # The weight is equal to 1 if the term exist in the doc, 0 otherwise
            query_vector[word] = 0
            if word in doc.vector:
                query_vector[word] = 1
        return query_vector

    def __get_inner_product(self, doc_vector, query_vector):
        inner_product = 0
        for term in doc_vector:
            if term in query_vector:
                inner_product += (doc_vector[term] * query_vector[term])
        return inner_product

    def __cos(self, doc, query):
        inner_product = self.__get_inner_product(doc.vector, query.vector)
        norm_doc = doc.get_magnitude()
        norm_query = query.get_magnitude()
        similarity = 0
        if norm_query != 0 and norm_doc != 0:
            similarity = inner_product / (norm_doc * norm_query)
        return similarity

    def search(self, query_doc, doc):
        score = self.__cos(doc, query_doc)
        return score

    def __display_posting(self, word):
        first = True
        for posting in self.index[word]:
            posting_idx = str(self.index[word][posting])
            if posting_idx[-1] == ']':
                posting_idx = posting_idx[:-1]
            if posting_idx[0] == '[':
                posting_idx = posting_idx[1:]
            if not first:
                print(" | ", end='')
            print("D"+str(posting+1)+":"+posting_idx, end='')
            first = False

    def __display_postings(self, word, idx):
        spaces = ""
        for i in range(15 - len(word)):
            spaces += ' '
        print(word+spaces+"-> ", end='')
        self.__display_posting(word)
        print('\n', end='')

    def display_report(self, query, scores):
        print("query :" + query+"\n")
        max_nbr_term = 5
        for idx, score in enumerate(scores):
            nbr = 0
            print("id: D00"+str(score[0]+1))
            print("top 5 keywords:")
            for k, v in self.documents[score[0]].vector.items():
                if nbr >= max_nbr_term:
                    break
                self.__display_postings(k, score[0])
                nbr += 1
            nbr_unique = self.documents[score[0]].get_unique_keywords_nbr(self.index, score[0])
            print("number of unique keyword: "+str(nbr_unique))
            print("L2:"+str(self.documents[score[0]].get_magnitude()))
            print("similarity:"+str(score[1]))
            if idx >= 2:
                break

    def sort(self, query):
        words = self.parser.parse_doc(query)
        scores = {}
        doc_query = Document()
        if not words:
            print("Incorrect query :"+query+" please refer to the ReadMe for the expected format")
            return False
        for idx, doc in enumerate(self.documents):
            # Create a weights vector for the query based on the similarity with the document
            # Not taking care of the duplicate and number of occurrences (vocabulary is empty)
            doc_query.vector = self.__make_query_vector(words, doc)
            cos_value = self.search(doc_query, doc)
            scores[idx] = cos_value # Similarity score
        scores = [(k, scores[k]) for k in sorted(scores, key=scores.get, reverse=True)]
        self.display_report(query, scores)
