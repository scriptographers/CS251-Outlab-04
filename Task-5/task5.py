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
DPI        = 200 # Controls the quality of the saved image

# Using requests to fetch data
def getData(DATA_URL, DATA_PATH):
    req = requests.get(DATA_URL)
    content = req.content

    with open(DATA_PATH, "wb") as f:
        f.write(content)

# Preprocessing
def preprocess(df):
    dates = df["Date"]
    X = df["Total Deceased"]
    idx_start = np.where(dates == START_DATE)[0][0]
    X = X[idx_start:].to_numpy() # Required data
    return X

# Main

getData(DATA_URL, DATA_PATH) # Call this once per day and then for subsequent uses comment this out
df = pd.read_csv(DATA_PATH)
X  = preprocess(df)
N  = len(X)

# Constructing H(t):
H = X[1:]/X[:-1] # We can also use np.roll(X, -1)/X, but this is faster

t = np.linspace(1,N-1,N-1) # The time axis

# Linear Regression
inferences = LR(t, H)
m = inferences[0] # slope
c = inferences[1] # intercept
y_hat = m*t + c # fitted line

# Finding the approximate day where the lewitt's metric is 1
days_from_start = round((1 - c)/m) # y_hat = 1 at the end
print(days_from_start)

# Plotting
plt.scatter(t, H, s=0.85, label="H(t)")
plt.plot(t, y_hat, 'r', linewidth=0.5, label="Fitted line")
plt.hlines(1, t[0], t[-1], colors='black', linestyles='--', linewidth=0.5, label="H(t)=1")
plt.xlabel("Time (days from April 01, 2020)")
plt.ylabel("H(t)")
plt.legend(loc='best')
plt.title("Lewitt's Metric")
plt.savefig(PLOT_PATH, dpi=DPI)