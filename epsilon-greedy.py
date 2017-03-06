#*********************Epsilon greedy algorithm
# INPUT:          K, Reward function, Try times, Exploration probability epsilon
# OUTPUT:       Amount Rewards r

import numpy
import random as ran
from multi_armed_bandits import Bandits

class Epsilon_Greedy:
    def __init__(self, arms_num, try_times, epsilon):
        self.K               = arms_num
        self.T               = try_times
        self.epsilon      = epsilon
        self.bandits     = Bandits(self.K)
        print("every bandits:")
        print self.bandits.u

    def get_random_pi(self):
        k = int(ran.random() * self.K)
        return k

    def get_greedy_pi(self, Q):
        k = Q.index(max(Q))
        return k

    def compute_amount_rewards(self):
        #amount rewards
        r          = 0.0

        average_reward_Q           = [0.0 for i in xrange(self.K)]
        count                               = [0 for j in xrange(self.K)]

        for t in xrange(self.T):
            if ran.random()<self.epsilon:
                k             = self.get_random_pi()
                print("Random")
            else:
                k             = self.get_greedy_pi(average_reward_Q)
                print("Greedy")

            v = self.bandits.get_reward(k)
            r = r + v
            average_reward_Q[k] = (average_reward_Q[k] * count[k] + v) / (count[k] + 1)
            count[k] = count[k] + 1

            print('action                     =    ', k)
            print('v                             =    ', v)
            print("count[k]                  =   ", count[k])
            print('average_reward_Q =    ', average_reward_Q)

        return r


if __name__ == "__main__":
    fun                 = Epsilon_Greedy(3, 1000, 0.1)
    reward           = fun.compute_amount_rewards()
    print("reward= ", reward)
