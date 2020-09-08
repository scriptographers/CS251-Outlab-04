import numpy as np

DATA_PATH = "mumbai_data.csv"

data = np.genfromtxt(DATA_PATH, dtype=None, delimiter=',', encoding='utf-8')
header = data[0][1:] # All except 'Days'
header = header[:, None]
data = data[1:]
numeric_data = data[:, 1:].astype('float32')
means  = np.around(np.mean(numeric_data, axis=0)[:, None], 3)
sigmas = np.around(np.std(numeric_data, axis=0)[:, None], 3)
table  = np.hstack((header, means, sigmas))
new_header = np.array(["Field", "Mean", "Std. Dev."])
table = np.vstack((new_header, table))

for row in table:
    print(' '.join(row))