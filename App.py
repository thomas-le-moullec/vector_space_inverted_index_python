from Parser import Parser

'''
    The app below show an implementation of the VectorSpace api
'''

documents_file = "ressources\text_collection_100"


def run_app():
    #vector_space = VectorSpace()
    parser = Parser()
    docs_collection = parser.get_collection(documents_file)
    print(docs_collection)
    #vector_space.index()


if __name__ == '__main__':
    run_app()
