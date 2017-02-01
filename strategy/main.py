#! /use/bin/python
# -*- coding: utf-8 -*-


from strategy import Strategy
from utils import logger


def simulate_stick_to_one_strategy(sim, n):

    log = logger.SimulationLogger()

    for sim_num in range(1, sim+1):
        strategy = Strategy(n)
        current_strategy = strategy.choose_strategy()

        log.set_common_parameters(
            strategy=current_strategy,
            sim_num=sim_num
        )

        for trial_num in range(1, n+1):
            is_success = strategy.try_strategy()

            log.set_parameters(
                trial_num=trial_num,
                result=is_success
            )
            log.logging()

            if is_success:
                break


def simulation_change_strategy_if_fail(sim, n):

    for sim_num in range(1, sim+1):
        strategy = Strategy(n)
        for trial_num in range(1, n+1):
            strategy.choose_strategy()
            is_success = strategy.try_strategy()

            trial_log = strategy.get_trial_log()
            trial_log['simulation_num'] = sim_num
            trial_log['trial_num'] = trial_num

            # TODO: 結果ログを書き込む処理を作る

            if is_success:
                break

