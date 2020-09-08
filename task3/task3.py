import argparse
import numpy as np 
from PIL import Image
from scipy.cluster.vq import kmeans2

# Arguments parsing
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-inp", type=str, required=True)
parser.add_argument("--k", "-k", type=int, required=True)
parser.add_argument("--output", "-out", type=str, required=True)
args = parser.parse_args()
INP_PATH = args.input
OUT_PATH = args.output
K = args.k

# Pre-processing
inp_img = Image.open(INP_PATH)
inp_img = np.array(inp_img).astype(float) # Convert to numpy array
SHAPE = inp_img.shape
inp_img = inp_img.reshape(-1, SHAPE[-1]) # Retain last dimension (color channels) , flatten others.

# KMeans++ and constructing the output image
centroids, labels = kmeans2(inp_img, K, minit="++")
out_img = centroids[labels] # Index everything at once :)

# Post-processing
out_img = out_img.reshape(SHAPE)
out_img = np.round(out_img).astype('uint8') # Back to int

# Saving to output
out_img = Image.fromarray(out_img)
out_img.save(OUT_PATH)