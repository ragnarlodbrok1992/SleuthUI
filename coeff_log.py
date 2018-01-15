import os
import csv
from file import File
from pprint import pprint


class Coeff(File):

    def __init__(self, path_to_file):
        super(Coeff, self).__init__(path_to_file)


if __name__ == '__main__':
    # c2 = Coeff('Sleth3/Output/gdansk_not_valid_dir/') # DEBUG
    # print(os.getcwd()) # DEBUG

    c1 = Coeff('\\Sleuth3\\Output\\gdansk_cal\\coeff.log')
    print(c1.ptf)
    output_string = str()
    row_str = str()

    with open(c1.ptf, 'r+') as csvfile:
        coeffreader = csv.reader(csvfile, delimiter=' ')

        for row in coeffreader:
            row = filter(None, row)
            for elem in row:
                row_str += elem + ' '
            output_string += row_str + '\n'
            row_str = ''

    with open(c1.path + '\\output.txt', 'w+') as f:
        f.write(output_string)
        print('File written to output.txt!')
        f.close()
