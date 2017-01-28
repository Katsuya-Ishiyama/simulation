#! /usr/bin/python
# -*- coding: utf-8 -*-

from strategy import Strategy


strategy = Strategy(5)

print('Current Strategy:', strategy.current_strategy)
print('Tried Strategy:', strategy.tried_strategy)
print('Stocks of Strategy:', strategy.stock_of_strategy)

for i in range(10):

    print('---------------------------')
    print('Trial: {0}'.format(i + 1))
    print(strategy.choose_strategy())
    print('Trial result:', strategy.try_strategy())
    print('Current Strategy:', strategy.current_strategy)
    print('Tried Strategy:', strategy.tried_strategy)
    print('Stocks of Strategy:', strategy.stock_of_strategy)

