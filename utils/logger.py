import os
import re
import csv
import json
import datetime


class SimulationLogger(object):

    def __init__(self, file):

        if os.path.exists(file):
            raise ValueError('{0} is already exists.')

        self._filetype = check_type_of_log_file(file)
        self.logfile = file
        self.common_parameters = dict(
            simulation_date=datetime.datetime.now(),
            logged_num=0
        )
        self.parameters = dict()

    def add_common_parameters(self, **kwargs):

        for k, v in kwargs.items():
            self.common_parameters.setdefault(k, v)

    def add_parameters(self, **kwargs):

        for k, v in kwargs.items():
            self.parameters.setdefault(k, v)

    def append_common_parameters_to_parameters(self):

        for k, v in self.common_parameters.items():
            self.parameters.setdefault(k, v)

    def output_as_csv(self):

        self.append_common_parameters_to_parameters()

        if not self.common_parameters['logged_num']:
            self._csv_header = self.parameters.keys()

        with open(self.logfile, 'a') as f:
            writer = csv.writer(f)
            if not self.common_parameters['logged_num']:
                writer.writerow(self._csv_header)
            writer.writerow(self.parameters.values())

    def output_as_json(self):

        self.append_common_parameters_to_parameters()
        with open(self.logfile, 'a') as f:
            f.write(json.dumps(self.parameters))

    def logging(self):

        if self._filetype == 'csv':
            self.output_as_csv()
        elif self._filetype == 'log':
            self.output_as_json()
        else:
            raise TypeError('{0} cannot be handled.'.format(self.logfile))

        self.common_parameters['logged_num'] += 1
        self.parameters = dict()  # initialize


def check_type_of_log_file(file):

    if re.match(r'.+\.csv$', file):
        filetype = 'csv'
    elif re.match(r'.+\.log$', file):
        filetype = 'log'
    else:
        _extension = re.findall(r'+.\.(\s+)$', file)
        ValueError('{0} cannot be handled.', _extension[0])

    return filetype

