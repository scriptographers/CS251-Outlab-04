import numpy as np

DATA_PATH = "mumbai_data.csv"

# Preproccessing
data = np.genfromtxt(DATA_PATH, dtype=None, delimiter=',', encoding='utf-8')
header = data[0][1:]  # All except 'Days'
header = header[:, None]
data = data[1:]
numeric_data = data[:, 1:].astype('float32')

# Computation
means = np.around(np.mean(numeric_data, axis=0)[:, None], 3)
sigmas = np.around(np.std(numeric_data, axis=0)[:, None], 3)


def format_floats(val):
    try:
        float(val)
        return format(float(val), ".3f")
    except ValueError:
        return val


# Formatting
table = np.hstack((header, means, sigmas))
new_header = np.array(["Field", "Mean", "Std. Dev."])
table = np.vstack((new_header, table))
padding = len(max(table.ravel(), key=len))
padding = "{:" + str(padding) + "}"  # Adds right padding to values
for row in table:
    print(' '.join(padding.format(format_floats(val)) for val in row))
