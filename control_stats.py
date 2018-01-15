from file import File
import csv


class ControlStats(File):

    def __init__(self, path_to_file):
        super(ControlStats, self).__init__(path_to_file)


if __name__ == '__main__':

    cs1 = ControlStats('\\Sleuth3\\Output\\gdansk_cal\\control_stats.log')
    print(cs1.ptf)
    output_string = str()
    row_str = str()
    control_stats_dict = dict()
    dict_labels = list()

    with open(cs1.ptf, 'r+') as csvfile:
        control_status_reader = csv.reader(csvfile, delimiter=' ')

        for idx, row in enumerate(control_status_reader):
            if idx == 1:
                dict_labels = filter(None, row)
                print "Dict_labels: " + str(dict_labels)
            if idx >= 2:
                row = filter(None, row)
                print(row)
                for idx, label in enumerate(dict_labels):
                    print "Label: " + str(label)
                    # control_stats_dict[str(idx)][str(dict_labels[idx])] = row[idx]

    # print control_stats_dict
