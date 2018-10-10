from Parser import Parser
from VectorSpace import VectorSpace
from pathlib import Path

'''
    The app below show an implementation example of the VectorSpace api
'''

default_doc_file = "ressources/text_collection_3"


def get_collection(file_path):
    try:
        collection = Path(file_path).read_text()
    except (FileExistsError, FileNotFoundError, OSError):
        return None
    return collection


def run_app():
    collection = get_collection(default_doc_file)
    if collection is None:
        print("Collection Error: Check the filename.")
        return
    '''
    # Splitting the lines in the app is not optimized for performance
    # because we need to loop again to index every document / line in the vector space.
    # Nevertheless it is a good implementation and utilization of the vector space API.
    '''
    docs_collection = collection.splitlines()
    vector_space = VectorSpace(docs_collection)
    vector_space.index_collection()


if __name__ == '__main__':
    run_app()
