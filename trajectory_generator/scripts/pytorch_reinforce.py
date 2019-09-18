import argparse
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import matplotlib.pyplot as plt
from torch.distributions.multivariate_normal import MultivariateNormal


parser = argparse.ArgumentParser(description='PyTorch REINFORCE example')
parser.add_argument('--gamma', type=float, default=0.99, metavar='G',
                    help='discount factor (default: 0.99)')
parser.add_argument('--seed', type=int, default=543, metavar='N',
                    help='random seed (default: 543)')
parser.add_argument('--log-interval', type=int, default=1, metavar='N',
                    help='interval between training status logs (default: 1)')
parser.add_argument('--epochs', type=int, default=20,
                    help='number of epochs for training (default: 20)')
parser.add_argument('--batch-size', type=int, default=10, metavar='N',
                    help='input batch size for training (default: 1)')
parser.add_argument('--in-dim', type=int, default=4,
                    help='policy input dimension (default: 4)')
parser.add_argument('--out-dim', type=int, default=5,
                    help='policy output dimension (default: 1)')
parser.add_argument('--learning-rate', type=int, default=0.001,
                    help='learning rate of the optimizer')
args = parser.parse_args()

# torch.manual_seed(args.seed)

def update_graph(fig, ax, line, x_value, y_value):
    line.set_xdata(np.append(line.get_xdata(), x_value))
    line.set_ydata(np.append(line.get_ydata(), y_value))
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

live_plots = {
    "loss": {
        "fig": None,
        "ax": None,
        "line1": None
    },
    "reward": {
        "fig": None,
        "ax": None,
        "line1": None
    },
    "theta": {
        "fig": None,
        "ax": None,
        "line1": None
    }
}
plt.ion()
live_plots["loss"]["fig"] = plt.figure("Loss")
live_plots["loss"]["ax"] = live_plots["loss"]["fig"].add_subplot(2, 1, 1)
live_plots["loss"]["line1"], = live_plots["loss"]["ax"].plot([], [], 'o-r', label="TRAIN Loss")

live_plots["reward"]["fig"] = live_plots["loss"]["fig"]
live_plots["reward"]["ax"] = live_plots["loss"]["fig"].add_subplot(2, 1, 2)
live_plots["reward"]["line1"], = live_plots["reward"]["ax"].plot([], [], 'o-b', label="Reward")


live_plots["loss"]["ax"].legend()
live_plots["reward"]["ax"].legend()


class Policy(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(Policy, self).__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim

        self.fc1 = nn.Linear(self.in_dim, 24)
        
        self.fc21 = nn.Linear(24, 24)  # mean layer
        self.fc31 = nn.Linear(24, self.out_dim)

        self.fc22 = nn.Linear(24, 24)  # log_var layer
        self.fc32 = nn.Linear(24, self.out_dim)

        self.saved_log_probs = []
        self.rewards = []
    
    def encode(self, x):
        h = F.relu(self.fc1(x))
        
        h21 = self.fc21(h)
        mean = self.fc31(h21)

        h22 = self.fc22(h)
        log_var = self.fc32(h22)

        return mean, log_var

    def forward(self, x):
        return self.encode(x)

policy = Policy(args.in_dim, args.out_dim)
optimizer = optim.Adam(policy.parameters(), lr=args.learning_rate)
eps = np.finfo(np.float32).eps.item()


def select_action(state):
    mean, log_var = policy(state)
    std = torch.exp(0.5*log_var)
    print ("mean = {} - var = {}".format(mean.data, torch.exp(log_var).data))

    cov_matrix = torch.diag(torch.tensor([0.001]*policy.out_dim))
    # cov_matrix = torch.diag(torch.exp(log_var))
    dist = MultivariateNormal(mean, cov_matrix)

    action_sample = dist.sample()

    log_prob = dist.log_prob(action_sample)
    policy.saved_log_probs.append(log_prob)
    return action_sample


def finish_episode():
    R = 0
    policy_loss = []
    returns = []
    for r in policy.rewards[::-1]:
        # R = r + args.gamma * R
        # returns.insert(0, R)
        returns.insert(0, r)
    returns = torch.tensor(returns)
    # returns = (returns - returns.mean()) # baseline
    returns = (returns - returns.mean()) / (returns.std() + eps) # baseline and normalization
    for log_prob, R in zip(policy.saved_log_probs, returns):
        policy_loss.append(-log_prob * R)
    optimizer.zero_grad()
    policy_loss = torch.stack(policy_loss).sum()
    policy_loss.backward()
    optimizer.step()
    del policy.rewards[:]
    del policy.saved_log_probs[:]
    return policy_loss

def execute_action(action):
    error = False
    reward = -(abs(action)).sum().pow(4).item() * 100
    return error, reward


def main():
    starting_state = torch.ones(policy.in_dim)
    for i_episode in range(args.epochs):
        reward = 0
        for t in range(0, args.batch_size):  # Don't infinite loop while learning

            action = select_action(starting_state)
            error, reward = execute_action(action)
            policy.rewards.append(reward)

        loss = finish_episode()

        if i_episode % args.log_interval == 0:
            print('Episode {}\tLast reward: {:.2f}'.format(
                  i_episode, reward))
            update_graph(live_plots["loss"]["fig"], live_plots["loss"]["ax"], live_plots["loss"]["line1"], i_episode, loss.item())
            update_graph(live_plots["reward"]["fig"], live_plots["reward"]["ax"], live_plots["reward"]["line1"], i_episode, reward)
    
    plt.show()


if __name__ == '__main__':
    main()
