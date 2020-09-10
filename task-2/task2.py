import argparse
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True)

args = parser.parse_args()  # Argument Parser


# Needed for legend label of epsilon-greedy is different,
def lbl(algo):  # parameter is tuple of (algorithm, epsilon)
    if algo[1] == 0:
        return algo[0]
    else:
        return '{} with epsilon={}'.format(*algo)


data = pd.read_csv(args.data)  # Read the data
instances = data.groupby('instance')  # Group by instances
for ist_name, data_ins in instances:  # Loop around these instances, in testcase 3
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('horizon')
    ax.set_ylabel('Regret')
    ax.set_title('Instance {} - both axes in log scale'.format(ist_name[2]))
    algorithms = data_ins.groupby(['algorithm', 'epsilon'])  # Group by algorithm and epsilon
    for algo_name, data_algo in algorithms:  # Loop around these algorithms, in testcase 7
        x, y = [], []  # Alternative methods crashing
        for horizon, data_horizon in data_algo.groupby('horizon'):
            x.append(horizon), y.append(data_horizon['REG'].sample(n=50).mean())  # Sampled 50 random values
        ax.loglog(x, y, label=lbl(algo_name))  # Loglog plot using matplotlib
    plt.legend()
    plt.savefig('instance{}.png'.format(ist_name[2]))
