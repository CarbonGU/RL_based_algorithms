# ************** Value Iteration *************
# Assuming Model is known
# Value Iteration is speed-efficient, which dose not wait value function for full convergence
# INPUT:             MDP <X, A, P, R> and Max time step T
# OUTPUT:          Optimal Policy pi, Optimal Value function

import numpy as np
import random as ran
from grid_mdp import Grid_Mdp

class VALUE_ITERATION:
    def __init__(self, grid_mdp):

        self.v    = [0.0 for i in xrange(len(grid_mdp.states))]

        self.pi   = dict()

        # Init random policy
        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states: continue
            self.pi[state] = grid_mdp.actions[0]

    def value_iteration_bellman(self, grid_mdp):
        for i in xrange(1000):
            delta = 0.0
            for state in grid_mdp.states:
                if state in grid_mdp.terminal_states: continue

                # start
                a1               = grid_mdp.actions[0]
                t, next_s, r  = grid_mdp.transform(state, a1)
                v1               = r + grid_mdp.gamma * self.v[next_s]
                # loop
                for action in grid_mdp.actions:
                    t, next_s, r    = grid_mdp.transform(state, action)
                    if v1 < r + grid_mdp.gamma * self.v[next_s]:
                        a1 = action
                        v1 = r + grid_mdp.gamma * self.v[next_s]

                delta                   += abs(self.v[state] - v1)
                self.v[state]           = v1
                self.pi[state]          = a1

            if delta < 1e-6:
                break


if __name__ == "__main__":
    my_grid_mdp       = Grid_Mdp()
    my_policy_value   = VALUE_ITERATION(my_grid_mdp)
    my_policy_value.value_iteration_bellman(my_grid_mdp)

    print("value:", my_policy_value.v)
    print("policy:", my_policy_value.pi)