import numpy as np

# Constants
DATA1_PATH = "mumbai_data.csv"
DATA2_PATH = "mumbai_unlock.csv"
SAVE_PATH = "info_combine.csv"

# Preproccessing
data1 = np.loadtxt(DATA1_PATH, skiprows=1, usecols=(1, 2), delimiter=',', encoding="utf-8")
data2 = np.loadtxt(DATA2_PATH, skiprows=1, usecols=(1, 2), delimiter=',', encoding="utf-8")
days = np.loadtxt(DATA1_PATH, skiprows=1, dtype=str, usecols=(0), delimiter=',', encoding="utf-8")

# Computations
infected_lock = data1[:, 1]
infected_unlock = data2[:, 1]
tests_lock = data1[:, 0]
tests_unlock = data2[:, 0]
pos_lock = infected_lock / tests_lock
pos_unlock = infected_unlock / tests_unlock

# Formatting
numeric = np.around(np.column_stack((infected_unlock, infected_lock, pos_lock, pos_unlock)), 3)  # Round off till 3 decimal places
table = np.column_stack((days, numeric))
header = np.asarray(["Day", "Infected(Unlock)", "Infected(Lock)", "Positivity Rate(Lock)", "Positivity Rate(Unlock)"], dtype=str)
table = np.vstack((header, table))

# Saving as CSV
np.savetxt(SAVE_PATH, table, fmt="%s", delimiter=',', encoding="utf-8")
