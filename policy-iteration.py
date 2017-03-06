# ************** Policy Iteration ***********
# Assuming Model is known, and will not interact with environment
# INPUT:             MDP <X, A, P, R> and Max time step T
# OUTPUT:          Optimal Policy pi

import numpy as np
import random as ran
from grid_mdp import Grid_Mdp

class Policy_Value:
    def __int__(self, grid_mdp):

        self.v    = [0.0 for i in xrange(len(grid_mdp.states))]

        self.pi   = dict()

        # Init random policy
        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states: continue
            self.pi[state] = grid_mdp.actions[0]


    def policy_evaluate(self, grid_mdp):
        for i in xrange(1000):

            delta = 0.0
            for state in grid_mdp.states:
                if state in grid_mdp.terminal_states: continue

                action            = self.pi[state]
                t, next_s, r    = grid_mdp.transform(state, action)
                new_v           = r + grid_mdp.gamma * self.v[next_s]
                delta            += abs(self.v[state] - new_v)
                self.v[state]   = new_v

            if delta < 1e-6:
                break

    def policy_improve(self, grid_mdp):
        policy_stable = True
        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states: continue

            b                 = self.pi[state]

            a1               = grid_mdp.actions[0]
            t, next_s, r  = grid_mdp.transform(state, a1)
            v1               = r + grid_mdp.gamma * self.v[next_s]

            for action in grid_mdp.actions:
                t, next_s, r    = grid_mdp.transform(state, action)
                if v1 < r + grid_mdp.gamma * self.v[next_s]:
                    a1 = action
                    v1 = r + grid_mdp.gamma * self.v[next_s]

            self.pi[state] = a1

            if b != self.pi[state]:
                policy_stable = False

        return policy_stable

    def policy_iteration(self, grid_mdp):
        print grid_mdp.states
        for i in xrange(100):
            self.policy_evaluate(grid_mdp)
            self.policy_improve(grid_mdp)


if __name__ == "__main__":
    grid_mdp         = Grid_Mdp()
    policy_value     = Policy_Value(grid_mdp)
    policy_value.policy_iteration(grid_mdp)
    print("value:", policy_value.v)
    print("policy:", policy_value.pi)

