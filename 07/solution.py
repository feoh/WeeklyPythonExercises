import os
from pathlib import Path
import pprint

def file_length(filename):
    return os.stat(filename).st_size


def filefunct(target_dir, func):
    success = {}
    failure = {}
    for dir, _, files in os.walk(target_dir):
        for file in files:
            full_path = Path(target_dir) / Path(dir) / Path(file)
            try:
                success[full_path] = func(full_path)
            except Exception as excpt:
                failure[full_path] = excpt
    return (success, failure)


if __name__ == '__main__':
    success, failure = filefunct('/etc', file_length)
    print("Successes:")
    pprint.pprint(success)
    print("Failures:")
    pprint.pprint(failure)
