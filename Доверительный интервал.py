import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import random


population = stats.norm.rvs(loc = 2, scale = 5, size = 4000)
sample_size = 4000
sample = np.random.choice(a = population, size = sample_size)


sample_mean = sample.mean()
st_dev = population.std()

def compute_si(sample, st_dev):
    z_value = stats.norm.ppf(q = 0.975)
    sample_size = len(sample)
    interval = z_value * (st_dev/np.sqrt(sample_size))
    conf_inv = (sample_mean - interval, sample_mean + interval)
    
    return conf_inv

print(compute_si(sample, st_dev))
