#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Jan 27 18:31:59 2017

@author: katsuya.ishiyama
"""


from numpy import random


class Strategy():

    def __init__(self, n):

        self._n = n

        _success_prob = random.sample(n)
        _strategy = {(i + 1): p for i, p in enumerate(_success_prob)}

        self.strategy = _strategy
        self.stock_of_strategy = _strategy.keys()
        self.tried_strategy = []
        self.current_strategy = None

    def _add_chosen_strategy(self, x):

        self.choose_strategy.append(x)

    def _delete_strategy_from_stock(self, x):

        self.stock_of_strategy.pop(x)

    def choose_strategy(self):

        # TODO: 手持ちの戦略を使い果たした場合の例外処理を書く
        if not self.stock_of_strategy:
            raise

        _chosen_id = random.choice(self.stock_of_strategy, 1)[0]

        self.current_strategy = _chosen_id
        self._delete_strategy_from_stock(_chosen_id)
        self._add_chosen_strategy(_chosen_id)

    def try_strategy(self):

        # TODO: 戦略に挑戦した結果を返す処理を書く
        pass


if __name__ == '__main__':

    strategy = Strategy(5)

    for i in range(10):
        strategy.choose_strategy()
        print strategy.chosen_strategy_id

