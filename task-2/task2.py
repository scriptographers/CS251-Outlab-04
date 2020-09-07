import argparse
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True)

args = parser.parse_args()


def lbl(algo):
    if algo[1] == 0:
        return algo[0]
    else:
        return '{} with epsilon={}'.format(*algo)


data = pd.read_csv(args.data)
instances = data.groupby('instance')
for ist_name, data_ins in instances:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('horizon')
    ax.set_ylabel('Regret')
    ax.set_title('Instance {} - both axes in log scale'.format(ist_name[2]))
    algorithms = data_ins.groupby(['algorithm', 'epsilon'])
    for algo_name, data_algo in algorithms:
        ax.loglog(data_algo.groupby('horizon')['REG'].mean(), label=lbl(algo_name))
    plt.legend()
    plt.savefig('instance{}.png'.format(ist_name[2]))
