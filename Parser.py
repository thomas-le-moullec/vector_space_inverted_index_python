from pathlib import Path


class Parser:
    def __init__(self):
        pass

    def get_collection(self, file_path):
        print(file_path)
        try:
            collection = Path(file_path).read_text()
        except (FileExistsError, FileNotFoundError, OSError):
            return None
        return collection
