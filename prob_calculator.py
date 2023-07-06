import copy
from random import choice

class Hat:
    def __init__(self, **kwargs):
        res = []
        for k, v in kwargs.items():
            for _ in range(v):
                res.append(k)

        self.contents = res


    def draw(self, number):
        res = []

        if number >= len(self.contents):
            res = self.contents
            self.contents.clear()
        else:
            for _ in range(number):
                tmp = choice(self.contents)
                res.append(tmp)
                self.contents.remove(tmp)
        
        return res


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for _ in range(num_experiments):
        hat_for_exp = copy.deepcopy(hat)
        drawed_balls = hat_for_exp.draw(num_balls_drawn)
        J = 0
        for k, v in expected_balls.items():
            if v <= drawed_balls.count(k):
                J += 1
            if J == len(expected_balls):
                M += 1

    probability = M/num_experiments
    return probability

