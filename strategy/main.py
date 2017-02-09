#! /use/bin/python
# -*- coding: utf-8 -*-


from strategy.strategy import Strategy
from utils import logger


LOGFILE = 'logfile path'


def simulate_stick_to_one_strategy(sim, n):

    log = logger.SimulationLogger(LOGFILE)

    for sim_num in range(1, sim+1):
        strategy = Strategy(n)
        current_strategy = strategy.choose_strategy()

        log.add_common_parameters(
            strategy=current_strategy,
            sim_num=sim_num
        )

        for trial_num in range(1, n+1):
            is_success = strategy.try_strategy()

            log.add_parameters(
                trial_num=trial_num,
                result=is_success
            )
            log.logging()

            if is_success:
                break


def simulation_change_strategy_if_fail(sim, n):

    log = logger.SimulationLogger(LOGFILE)

    for sim_num in range(1, sim+1):
        strategy = Strategy(n)

        log.add_common_paramerets(sim_num=sim_num)

        for trial_num in range(1, n+1):
            current_strategy = strategy.choose_strategy()
            is_success = strategy.try_strategy()

            log.add_parameters(
                trial_num=trial_num,
                strategy=current_strategy,
                result=is_success
            )
            log.logging()

            if is_success:
                break

def main():

    simulate_stick_to_one_strategy(sim=3, n=5)
    simulation_change_strategy_if_fail(sim=3, n=5)


main()

