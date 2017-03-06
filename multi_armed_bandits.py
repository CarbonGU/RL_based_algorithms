import random as ran

class Bandits:
    def __init__(self, arms_num):
        if arms_num<2:
            raise Exception("arms num at least 2 ")
        every_u           = [ran.random() for i in xrange(arms_num)] #probability of every arms to return coins
        sum_u             = sum(every_u)
        self.u               = [every_u_j / sum_u for every_u_j in every_u]

    def get_reward(self, action):
        if action<0 or action>len(self.u):
            raise Exception("Invalid action %d"%action)

        r = ran.random()
        if r<=self.u[action]:
            return 1
        else:
            return 0

