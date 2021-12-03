from gym import Env


class BoardEnv(Env):

    def __init__(self):

        self.size = (10, 10)  # (x_position, y_position) - size of the board - tuple - fixed
        self.item_pickup_pos = (0, 0)  # (x_position, y_position) - tuple - fixed
        self.item_drop_off_pos = (9, 9)  # (x_position, y_position) - tuple - fixed

        self.carrier_pos = (9, 0)  # (x_position, y_position) - tuple - not fixed
        self.is_item_in_carrier = False  # [False, True] - not fixed

        self.action_space = [0, 1, 2, 3, 4, 5]  # go up / go down / go left / go right / pick up / drop off

        self.state_space = []
        for x_pos_carrier in range(self.size[0]):
            for y_pos_carrier in range(self.size[1]):
                for item_in_carrier in range(2):
                    self.state_space.append((x_pos_carrier, y_pos_carrier, item_in_carrier))

    def step(self, action):

        if action == 0:  # Go down
            if self.carrier_pos[1] == self.size[1] - 1:
                reward = -10
                done = False
            else:
                self.carrier_pos = (self.carrier_pos[0], self.carrier_pos[1] + 1)  # Update position
                reward = -1
                done = False

        elif action == 1:  # Go up
            if self.carrier_pos[1] == 0:
                reward = -10
                done = False
            else:
                self.carrier_pos = (self.carrier_pos[0], self.carrier_pos[1] - 1)  # Update position
                reward = -1
                done = False

        elif action == 2:  # Go left
            if self.carrier_pos[0] == 0:
                reward = -10
                done = False
            else:
                self.carrier_pos = (self.carrier_pos[0] - 1, self.carrier_pos[1])  # Update position
                reward = -1
                done = False

        elif action == 3:  # Go right
            if self.carrier_pos[0] == self.size[0] - 1:
                reward = -10
                done = False
            else:
                self.carrier_pos = (self.carrier_pos[0] + 1, self.carrier_pos[1])  # Update position
                reward = -1
                done = False

        elif action == 4:  # Pick up item
            if not self.is_item_in_carrier and self.carrier_pos == self.item_pickup_pos:
                self.is_item_in_carrier = True
                reward = 20
                done = False
            else:
                reward = -10
                done = False

        elif action == 5:  # Drop off item
            if self.is_item_in_carrier and self.carrier_pos == self.item_drop_off_pos:
                self.is_item_in_carrier = False
                reward = 20
                done = True
            else:
                reward = -10
                done = False

        state = (self.carrier_pos[0], self.carrier_pos[1], int(self.is_item_in_carrier))

        info = {}

        return state, reward, done, info

    def render(self):
        pass

    def reset(self):
        """
        Resets the environment for a new episode.
        """

        self.carrier_pos = (9, 0)
        self.is_item_in_carrier = False
        state = (self.carrier_pos[0], self.carrier_pos[1], int(self.is_item_in_carrier))
        return state
