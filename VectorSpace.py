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
        print(words)
        if not words:
            print("In collection Doc ID :"+str(idx_doc)+" the document will not be treated."+document)
            return False
        self.documents.append(Document())
        for idx_term, term in enumerate(words):
            self.index_term(term, idx_term, idx_doc)
        self.__make_doc_vector(idx_doc)
        self.documents[idx_doc].vector = [(k, self.documents[idx_doc].vector[k]) for k in sorted(self.documents[idx_doc].vector, key=self.documents[idx_doc].vector.get, reverse=True)]
        return True

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
        return True

    def get_weight(self, word, doc):
        score = 0
        term_frequency = doc.vocabulary[word] / len(doc.vocabulary)
        max_term_frequency_key, max_term_frequency_value = doc.vocabulary.most_common(1)[0]
        max_term_frequency_value = max_term_frequency_value / len(doc.vocabulary)
        doc_frequency = len(self.index[word])
        doc_nbr = len(self.documents)

        '''print("Term Frequency:"+str(term_frequency))
        print("Max term frequency:"+str(max_term_frequency_value))
        print("Doc frequency:"+str(doc_frequency))
        print("Doc Total number:"+str(doc_nbr))'''
        score = self.transform.rank(term_frequency, max_term_frequency_value, doc_frequency, doc_nbr)
        return score

    def __make_doc_vector(self, idx_doc):
        for term in self.documents[idx_doc].vocabulary.keys():
            self.documents[idx_doc].vector[term] = self.get_weight(term, self.documents[idx_doc])
            print(self.documents[idx_doc].vector)

    def __make_query_vector(self, search, doc):
        query_vector = {}
        for word in search:
            query_vector[word] = 0
            if word in doc.vector:
                query_vector[word] = 1
        return query_vector

    def __get_inner_product(self, doc_vector, query_vector):
        inner_product = 0
        for term in doc_vector:
            if term in query_vector:
                inner_product += doc_vector[term] * query_vector[term]
        return inner_product

    def __cos(self, doc_vector, query_vector):
        inner_product = self.__get_inner_product(doc_vector, query_vector)
        similarity = inner_product / (len(doc_vector)* len(query_vector))
        return similarity

    def search(self, search, doc):
        query_vector = self.__make_query_vector(search, doc)
        return self.__cos(doc.vector, query_vector)

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

    def display_report(self, query, idx, doc):
        print("query :" + query+"\n")
        print("id: " + str(idx + 1))
        print("top 5 keywords:")
        for i in range(5):
            self.__display_postings(doc.vector[i][0], idx)
        nbr_unique = doc.get_unique_keywords_nbr()
        print("number of unique keyword: "+str(nbr_unique))

    def sort(self, query):
        words = self.parser.parse_doc(query)
        scores = {}
        if not words:
            print("Incorrect query :"+query+" please refer to the ReadMe for the expected format")
            return False
        for idx, doc in enumerate(self.documents):
            if idx == 59:
                score = 0
                cos_value = self.search(words, doc)
                self.display_report(query, idx, doc)
            '''for word in words:
                if word in self.index and word in doc.vocabulary:
                    partial_score = self.get_score(word, doc)
                    print(partial_score)
                    score += partial_score
            scores[idx] = score
            print("Vector:")
            print(doc.vector)'''