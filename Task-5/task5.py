import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress as LR

# Constants
DATA_URL   = "https://api.covid19india.org/csv/latest/case_time_series.csv"
DATA_PATH  = "data.csv"
PLOT_PATH  = "covid.png"
START_DATE = "01 April " # Extra space at the end is important

def getData(DATA_URL, DATA_PATH):
    req = requests.get(DATA_URL)
    content = req.content

    with open(DATA_PATH, "wb") as f:
        f.write(content)

getData(DATA_URL, DATA_PATH)

# Preprocessing
df = pd.read_csv(DATA_PATH)
dates = df["Date"]
X = df["Total Deceased"]
idx_start = np.where(dates == START_DATE)[0][0]
X = X[idx_start:].to_numpy() # Required data
N = len(X)

# Constructing H(t): To be improved
H = np.zeros(N-1)
for i in range(N-1):
    H[i] = X[i+1]/X[i]

t = np.linspace(1,N-1,N-1)

# Linear Regression
inferences = LR(t, H)
slope = inferences[0]
intercept = inferences[1]
fitted_line = slope*t + intercept

# Finding the approximate day where the lewitt's metric is close to 1
# eps = 10**(-3) # (y-eps,y+eps)
# idx_stop = np.where(abs(fitted_line - 1) < eps)[0][0]
# days_from_start = t[idx_stop]
# print(int(days_from_start))
days_from_start = round((1 - intercept)/slope) # y = 1 at the end
print(days_from_start)

# Plotting
plt.plot(t, H, label="H(t)")
plt.plot(t, fitted_line, label="Fitted line")
plt.xlabel("Time (days from April 01, 2020)")
plt.ylabel("H(t)")
plt.legend(loc='best')
plt.title("Lewitt's Metric")
plt.savefig(PLOT_PATH, dpi=300)






