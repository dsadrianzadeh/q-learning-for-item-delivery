import random
import numpy as np


class Agent:

    def __init__(self, alpha, epsilon, gamma, state_space, action_space):

        # Step I of the Q-learning algorithm
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.state_space = state_space
        self.action_space = action_space
        self.length_of_action_space = len(self.action_space)

        # Step II of the Q-learning algorithm
        self.Q = {}
        for state in self.state_space:
            self.Q[state] = [0 for _ in range(self.length_of_action_space)]

    def policy(self, state):

        if random.uniform(0, 1) < self.epsilon:
            action = self.action_space[random.randint(0, self.length_of_action_space - 1)]
        else:
            action = np.argmax(self.Q[state])

        return action

    def update_policy(self, state, action, reward, state_):

        self.Q[state][action] = self.Q[state][action] + self.alpha * (reward + self.gamma * np.max(self.Q[state_])
                                                                      - self.Q[state][action])
