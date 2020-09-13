import numpy as np

# Constants
DATA_PATH = "mumbai_data.csv"
SAVE_PATH = "transformed.csv"
POPULATION = 20.4  # Population of Mumbai (in Millions)

# Preproccessing
data = np.genfromtxt(DATA_PATH, dtype=None, delimiter=',', encoding="utf-8")
header = data[0].astype("U50")  # Unicode 50 character string
data = data[1:]
days = data[:, 0]
X = data[:, 1:].astype("float32")

# Computation
X[:, 1] /= X[:, 0]  # Test positivity rate
X[:, 0] = np.round(X[:, 0] / POPULATION)  # Tests per Million (To nearest integer)
X = np.around(X, 3)  # Round off to same no. of digits

# Formatting
header[1] = "Tests per Million"
header[2] = "Test Positivity rate"
table = np.hstack((days[:, None], X[:, 0:1].astype("int"), X[:, 1:2], X[:, 2:].astype("int")))
table = np.vstack((header, table))

# Saving as CSV
np.savetxt(SAVE_PATH, table, fmt="%s", delimiter=',', encoding="utf-8")
