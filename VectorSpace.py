from Parser import Parser
from transform import TfIdf


class VectorSpace:

    def __init__(self, dictionnaries=[], transforms = [TfIdf]):
        self.dictionnaries = dictionnaries
        self.transforms = transforms
        self.doc_id = 0
        self.parser = Parser()
        self.index = {}

    def index_term(self, term, idx_term, idx_doc):
        if term[-1] == 's':
            term = term[:-1]
        if term not in self.index:
            self.index[term] = {}
        if idx_doc not in self.index[term]:
            self.index[term][idx_doc] = []
        self.index[term][idx_doc].append(idx_term)

    def index_document(self, document, idx_doc):
        words = self.parser.parse_doc(document)
        if not words:
            print("In collection Doc ID :"+str(idx_doc)+" the document will not be treated.")
            return False
        for idx_term, term in enumerate(words):
            self.index_term(term, idx_term, idx_doc)
            print("This is document DID:" + str(idx_doc) + " term["+str(idx_term)+"] value:---"+term+"---")
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
        print(self.index)
        return True


