import os
import numpy as np 
from A2C import AdvantageActorCritic, generate_session
import gym
import matplotlib.pyplot as plt
from tqdm import tqdm


if __name__ == '__main__':
	
	env = gym.make("CartPole-v0").env
	n_action = env.action_space.n 
	state_shape = env.observation_space.shape
	steps = 100
	t_max = 100
	agent = AdvantageActorCritic(state_shape, n_action, steps)
	agent.sess.run(agent.init)
	save_path = os.path.join(os.path.dirname(__file__))
	Rewards = []
	for epoch in tqdm(range(t_max)):
		sum_reward = 0
		for _ in range(steps):
			r = generate_session(env, agent)
			sum_reward += r
		mean_reward = sum_reward / steps
		Rewards.append(mean_reward)
		agent.save_model(save_path)
		if mean_reward > 300:
			print('You Win')
			print(f'Epoch: {epoch} | mean rewards : {mean_reward}')
			plt.title('mean Game rewards')
			plt.xlabel('Epoch Game')
			plt.ylabel('mean reward')
			plt.plot(Rewards)
			plt.show()
			plt.close()
			break