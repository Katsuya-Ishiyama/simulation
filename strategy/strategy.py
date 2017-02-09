#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Jan 27 18:31:59 2017

@author: katsuya.ishiyama
"""


from numpy import random


# Definition of module level constants
SUCCESS_CODE = 1
FAILURE_CODE = 0


class Strategy():

    def __init__(self, n):

        _success_probability = _generate_success_probability(n)
        _strategy = {i: p for i, p in enumerate(_success_probability, 1)}

        self._n = n
        self.strategy = _strategy
        self.stock_of_strategy = list(_strategy.keys())
        self.tried_strategy = []
        self.current_strategy = None
        self.previous_strategy = None
        self.count_same_strategy = 0
        self._result_of_trial = None

    def choose_strategy(self):

        if not self.stock_of_strategy:
            raise ValueError('There is no strategy in stock.')

        _chosen_id = random.choice(self.stock_of_strategy, 1)[0]

        self.previous_strategy = self.current_strategy
        self.current_strategy = _chosen_id
        self.count_same_strategy = 0
        self.stock_of_strategy.remove(_chosen_id)

        _chosen_strategy = {
            'chosen_strategy': _chosen_id,
            'success_probability': self._get_success_probability()
        }

        return _chosen_strategy

    def _get_success_probability(self):

        return self.strategy[self.current_strategy]

    def try_strategy(self):

        if not self.current_strategy:
            raise ValueError('No strategy is chosen.')

        self.tried_strategy.append(self.current_strategy)

        self._result_of_trial = _get_trial_result(
            p=self._get_success_probability()
        )

        if self.current_strategy == self.previous_strategy:
            self.count_same_strategy += 1

        return self._result_of_trial



def _get_trial_result(p):

    _trial_result = random.choice([FAILURE_CODE, SUCCESS_CODE], size=1, p=[1 - p, p])

    return _trial_result[0]


def _generate_success_probability(size):

    return random.sample(size)

