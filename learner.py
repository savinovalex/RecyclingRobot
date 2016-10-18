import numpy as np
import matplotlib.pyplot as plt
import random
from model import *
from enviroment import *


gamma_fading = 0.98
exploration = 0.09

field_size = (20, 20)
start_point = (18, 5)
target_point = (3, 10)

value_func = [[0 for x in range(field_size[0])] for y in range(field_size[1])]  # 2-dim matrix filled 0
quantity_of_visits = [[0 for x in range(field_size[0])] for y in range(field_size[1])]  # 2-dim matrix filled 0

model = RecyclingModel(field_size)
enviroment = RecyclingEnviroment(field_size, start_point, target_point)


def softmax(w):
    e = np.exp(w)
    dist = e / np.sum(e)
    return dist

class GreedyPolicy:
    def __init__(self):
        pass


    def choose_action(self, s):
        actions = []
        actionValues = []

        for a in model.actions:
            s_new = model.get_new_state(s, a)
            if s_new != None:
                actions.append(a)
                actionValues.append(value_func[s_new[0]][s_new[1]])

        probs = softmax(actionValues)

        if random.random() < exploration:
            return random.choice(actions)

        total = 0
        rnd = random.random()
        for i, prob in enumerate(probs):
            total += prob
            if rnd < total:
                return actions[i]



    def learn(self, history):   # list of dictionaries
        reward = 0
        for node in reversed(history):
            s = node["state"]
            reward = node["reward"] + gamma_fading * reward
            value_func[s[0]][s[1]] += reward
#            if s[0] == target_point[0] + 1 and s[1] == target_point[1]:
#                print (reward)


policy = GreedyPolicy()

fig = plt.figure()

for round in range(100):
    history = []
    enviroment.reset()
    current_state = enviroment.get_current_state()
    quantity_of_visits[current_state[0]][current_state[1]] += 1

    while not enviroment.is_terminated():
        action = policy.choose_action(current_state)

        current_state, reward = enviroment.apply_action(action)

        quantity_of_visits[current_state[0]][current_state[1]] += 1

        history.append({
            "state": current_state,
            "reward": reward
        })


    policy.learn(history)
    print ("len=", len(history))

    if True or round % 3 == 0:
        fig.add_subplot(1, 2, 1)
        plt.imshow(value_func)

        fig.add_subplot(1, 2, 2)
        plt.imshow(quantity_of_visits)

        plt.show()
        plt.draw()

        #print (value_func[target_point[0] ][target_point[1]])





