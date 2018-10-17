import sys

from VectorSpace import VectorSpace
from pathlib import Path

'''
    The app below show an implementation example of the VectorSpace api
'''

default_doc_file = "resources/text_collection_100.txt"
default_queries_file = "resources/query_10.txt"


def get_collection(file_path):
    try:
        collection = Path(file_path).read_text()
    except (FileExistsError, FileNotFoundError, OSError):
        return None
    return collection


def run_app():
    collection = get_collection(default_doc_file)
    if collection is None:
        print("Collection documents Error: Check the filename.")
        return
    docs_collection = collection.splitlines()
    vector_space = VectorSpace(docs_collection)
    index_res = vector_space.index_collection()
    if not index_res:
        return False
    queries_collection = get_collection(default_queries_file)
    if queries_collection is None:
        print("Queries database Error: Check the filename.")
        return
    queries = queries_collection.splitlines()
    for query in queries:
        result = vector_space.sort(query)
        vector_space.display_report(query, result)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] is not None and sys.argv[2] is not None:
            default_doc_file = sys.argv[1]
            default_queries_file = sys.argv[2]
    run_app()
