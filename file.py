import os


class File(object):

    def __init__(self, path_to_file):
        abs_path_to_file = os.path.abspath(os.getcwd() + path_to_file)
        if os.path.exists(abs_path_to_file) and os.path.isfile(abs_path_to_file):
            self.ptf = abs_path_to_file
            self.path = os.path.dirname(abs_path_to_file)
        else:
            raise AssertionError('Path does not exist or is not file!', str(abs_path_to_file))
