from io import IOBase


class Tee:

    def __init__(self, fh1: IOBase, fh2: IOBase = None):
        self.file_handles = []
        self.file_handles.append(fh1)

        if fh2:
            self.file_handles.append(fh2)

    def write(self, string):
        for fh in self.file_handles:
            fh.write(string)

    def writelines(self, lines):
        self.write("".join(lines))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for fh in self.file_handles:
            fh.close()
