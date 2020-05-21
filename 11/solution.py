from hashlib import md5
import os.path


class DirFileHash:
    def __init__(self, dir_name):
        if not os.path.dirname(dir_name):
            raise ValueError

        self.dirname = dir_name

    def __getitem__(self, item):
        file_path = os.path.join(self.dirname, item)
        if not os.path.isfile(file_path):
            return None

        with open(file_path) as file_contents:
            contents = file_contents.read().encode()
            md5_contents = md5(contents)
            return md5_contents.hexdigest()
