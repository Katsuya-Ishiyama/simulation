import os
import re
import csv
import json
import datetime


class SimulationLogger(object):

    def __init___(self, file):

        self._filetype = _check_type_of_log_file(file)

        # TODO: file で指定されたファイルがすでに存在している場合は
        #       エラーを返す

        self.logfile = file
        self.common_parameters = dict(
            simulation_date=datetime.datetime.now(),
            logged_num=0
        )
        self.parameters = dict()

    def set_common_parameters(self, **kwargs):

        for k, v in kwargs.items():
            self.common_parameters.setdefault(k, v)

    def set_parameters(self, **kwargs):

        for k, v in kwargs.items():
            self.parameters.setdefault(k, v)

    def _output_as_csv(self):
        # collections の ChainMap を使うほうが早いか
        for k, v in self.common_parameters.items():
            self.parameters.setdefault(k, v)

        if not self.common_parameters['logged_num']:
            self._csv_header = self.parameters.keys()

        with open(self.logfile, 'a') as f:
            writer = csv.writer(f)
            if not self.common_parameters['logged_num']:
                writer.writerow(self._csv_header)
            writer.writerow(self.parameters.values())

    def logging(self, log):

        _log = log.copy()
        _log.update(self.common_parameters)

        if self.filetype == 'csv':
            self._output_as_csv()

        self.common_parameters['logged_num'] += 1
        self.parameters = dict()


def _check_type_of_log_file(file):

    if re.match(r'.+\.csv$', file):
        filetype = 'csv'
    elif re.match(r'.+\.log$', file):
        filetype = 'json'
    else:
        _extension = re.findall(r'+.\.(\s+)$', file)
        ValueError('{0} cannot be handled.', _extension[0])

    return filetype
