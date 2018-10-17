# Inverted_index Search Engine
>Basic search engine to sort similarity between a query and a list of documents

Parser.py: This is the class containing the methods in charge of the preprocessing. The VectorSpace class is implementing a Parser and parse the documents and terms thanks to it.

VectorSpace.py: This is the main class of the API which is implementing the Transform, the Similarity, the Parser and a list of Document. Few important methods for the developer who use the API:
* index_collection : Index a collection of documents in the inverted index. If no collection were given at the VectorSpace initialisation, the index_collection method can take a collection in argument.
* index_document : Index only one document. Need a document and a doc ID
* index_term : Index only a term. Need a term, a doc ID and a term ID
* sort : Take a query as parameter and return a sorted dictionary of similarity scores between this query and the indexed documents.
* display_report : Take a query and the sorted dictionary of similarity. Useful to print in a good format the result of the sort.

App.py: A good example of the API implementation. It is basically getting the collection of documents and queries. Calling the index_collection and then in a loop it is calling the sort and the display.

## Help and Environment
This project has been realized with Python 3.7.0 on Windows Pro 10.0.17134 Build 17134.
Run successfully on Linux and OSX

There is no libraries or packages

## To run the program (2 possibilities): 
* python App.py
* python App.py resources/text_collection_100.txt resources/query_10.txt

>The solution 1 will open the default files defined in the App.py file.
In the solution 2, the first argument is the documents collection and the second is the queries collection. You can put only one argument and the queries collection will be the one defined in App.py


thomas.le-moullec:
https://github.com/thomas-le-moullec/vector_space_inverted_index