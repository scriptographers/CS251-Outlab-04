import numpy as np

DATA_PATH = "mumbai_data.csv"
np.set_printoptions(precision=3) # Since 3 decimal places is asked

data = np.genfromtxt(DATA_PATH, dtype=None, delimiter=',', encoding='utf-8')
headers = data[0][1:] # All except 'Days'
data = data[1:]
numeric_data = data[:, 1:].astype('float32')
means  = np.mean(numeric_data, axis=0)
sigmas = np.std(numeric_data, axis=0)
print(headers)