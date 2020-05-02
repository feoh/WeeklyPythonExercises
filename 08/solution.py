def multiziperator(*args):
    zipped_list = zip(*args)
    unzipped_list = [item for sublist in zipped_list for item in sublist]
    for item in unzipped_list:
        yield item


