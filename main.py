from environment import BoardEnv
from agent import Agent

env = BoardEnv()

state_space = env.state_space
action_space = env.action_space

alpha = 0.1
epsilon = 0.1
gamma = 0.6

agent = Agent(alpha, epsilon, gamma, state_space, action_space)

episodes = 30000

for episode in range(1, episodes + 1):

    observation = env.reset()
    done = False
    total_reward = 0
    steps = 0

    actions = []

    while not done:

        # env.render()
        action = agent.policy(observation)
        observation_, reward, done, info = env.step(action)
        agent.update_policy(observation, action, reward, observation_)
        observation = observation_
        total_reward += reward
        steps += 1

        actions.append(action)

    print(f"============ Episode: {episode} ============")
    print(f"Total Reward: {total_reward}")
    print(f"Steps: {steps}")
    print(f"Actions: {actions}")

# env.close()
