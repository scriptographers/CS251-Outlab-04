import numpy as np

# Constants
DATA1_PATH = "mumbai_data.csv"
DATA2_PATH = "mumbai_unlock.csv"
SAVE_PATH = "info_combine.csv"

# Preproccessing
data1 = np.loadtxt(DATA1_PATH, skiprows=1, usecols=(1, 2), dtype=object, delimiter=',', encoding="utf-8")
data2 = np.loadtxt(DATA2_PATH, skiprows=1, usecols=(1, 2), dtype=object, delimiter=',', encoding="utf-8")
days = np.loadtxt(DATA1_PATH, skiprows=1, dtype=str, usecols=(0), delimiter=',', encoding="utf-8")

# Computations
infected_lock = data1[:, 1]
infected_unlock = data2[:, 1]
tests_lock = data1[:, 0]
tests_unlock = data2[:, 0]
pos_lock = np.around(infected_lock.astype(float) / tests_lock.astype(float), 3)
pos_unlock = np.around(infected_unlock.astype(float) / tests_unlock.astype(float), 3)

# Formatting
numeric = np.column_stack((infected_unlock, infected_lock, pos_lock, pos_unlock))  # Round off till 3 decimal places
table = np.column_stack((days, numeric))
header = np.asarray(["Day", "Infected(UnLock)", "Infected(Lock)", "Positivity Rate(Lock)", "Positivity Rate(UnLock)"], dtype=str)
table = np.vstack((header, table))

# Saving as CSV
np.savetxt(SAVE_PATH, table, fmt="%s", delimiter=',', encoding="utf-8")
