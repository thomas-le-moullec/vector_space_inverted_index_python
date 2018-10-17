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
    # Get the collection of documents / dictionaries
    collection = get_collection(default_doc_file)
    if collection is None:
        print("Collection documents Error: Check the filename.")
        return
    # Split the dictionaries on new line
    docs_collection = collection.splitlines()
    # Create the object VectorSpace and initialize it with the document collection we fetched before
    vector_space = VectorSpace(docs_collection)
    # Index the collection we gave during initialization
    index_res = vector_space.index_collection()
    if not index_res:
        return False
    # Get the collection of queries
    queries_collection = get_collection(default_queries_file)
    if queries_collection is None:
        print("Queries database Error: Check the filename.")
        return
    # Split the queries on newline
    queries = queries_collection.splitlines()
    for query in queries:
        # Foreach query, we sort it : Basically getting a dict of similarity scores
        result = vector_space.sort(query)
        # Then we can display the result of this array ; Creating a Dataclass would be preferable
        vector_space.display_report(query, result)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] is not None and sys.argv[2] is not None:
            default_doc_file = sys.argv[1]
            default_queries_file = sys.argv[2]
    run_app()
