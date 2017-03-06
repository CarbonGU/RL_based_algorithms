#*********************Softmax algorithm
# INPUT:          K, Reward function, Try times, Tempreture tao
# OUTPUT:       Amount Rewards r

import numpy as np
import random as ran
from multi_armed_bandits import Bandits

class Softmax:
    def __init__(self, arms_num, try_times, tao):
        self.K               = arms_num
        self.T               = try_times
        self.tao            = tao
        self.bandits     = Bandits(self.K)
        print("every bandits:")
        print self.bandits.u

    def boltzmann(self, Q):
        S           = sum([np.exp(Q_i / self.tao) for Q_i in Q])
        P           = [np.exp(Q_k / self.tao) / S for Q_k in Q]
        P_dist    = [0.0 for i in xrange(len(P))]
        for j in xrange(len(P)):
            if j == 0:
                P_dist[j] = P[j]
            else:
                P_dist[j] = P_dist[j-1] + P[j]

        return P_dist

    def get_policy(self, P_dist):
        prob = ran.random()
        print("prob:", prob)
        k = -1
        for i in xrange(len(P_dist)):
            if i == 0:
                if prob<=P_dist[i]:
                    k = 0
                    break
            else:
                if prob>P_dist[i - 1] and prob<=P_dist[i]:
                    k = i
                    break

        if k == -1:
            raise Exception("Can't find k!")

        return k



    def compute_amount_rewards(self):
        #amount rewards
        r          = 0.0

        average_reward_Q           = [0.0 for i in xrange(self.K)]
        count                               = [0 for j in xrange(self.K)]

        for t in xrange(self.T):
            P_dist                           = self.boltzmann(average_reward_Q)

            k                                  = self.get_policy(P_dist)

            v                                  = self.bandits.get_reward(k)
            r                                   = r + v
            average_reward_Q[k]   = (average_reward_Q[k] * count[k] + v) / (count[k] + 1)
            count[k]                       = count[k] + 1

            print('action  =    ', k)
            #print('v =    ', v)
            # print("count[k] =   ", count[k])
            print('average_reward_Q = ', average_reward_Q)
            print("P_dist:", P_dist)

        return r


if __name__ == "__main__":
    fun                 = Softmax(3, 1000, 0.1)
    reward           = fun.compute_amount_rewards()
   # print("reward= ", reward)
