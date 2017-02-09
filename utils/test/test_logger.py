# -*- coding: utf-8 -*-

import unittest
from collections import ChainMap
from utils import logger


class LoggerTestCase(unittest.TestCase):

    def setUp(self):
        self._logger = logger.SimulationLogger('~/test.log')

    def test_set_common_parameters(self):
        preseted_params = self._logger.common_parameters
        self._logger.set_common_parameters(a=1)
        self._logger.set_common_parameters(b=2, c=3)
        expected_params = dict(ChainMap(preseted_params, dict(a=1, b=2, c=3)))
        self.assertEqual(expected_params, self._logger.common_parameters)

    def test_set_parameters(self):
        self._logger.set_parameters(a=1)
        self._logger.set_parameters(b=2, c=3)
        expected_params = dict(a=1, b=2, c=3)
        self.assertEqual(expected_params, self._logger.parameters)

    def test_append_common_parameters_to_parameters(self):
        _common_params = self._logger.common_parameters
        self._logger.set_parameters(a=1, b=2)
        self._logger.append_common_parameters_to_parameters()
        expected_params = dict(ChainMap(_common_params, dict(a=1, b=2)))
        self.assertEqual(expected_params, self._logger.parameters)

    def test_output_as_csv(self):
        pass

    def test_output_as_json(self):
        pass

    def test_logging(self):
        pass

    def test_check_type_of_log_file(self):
        pass


unittest.main()

