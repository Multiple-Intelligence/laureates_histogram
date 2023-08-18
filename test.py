import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics as st
import pandas as pd

ages_frequencies = list()

loc = "data.csv"
ages_column = 'Ages'
leaurates_column = 'laureates'
# Read the CSV file into a DataFrame
data = pd.read_csv(loc)

ages = data[ages_column].values
laureates = data[leaurates_column].values
for i in range(len(ages)):
    ages_frequencies.extend([ages[i]] * laureates[i])

sample = [63, 74, 42, 73, 60, 64, 40, 51, 48, 71, 60, 62, 58, 56, 57, 71, 69, 84, 73, 61, 82, 85, 56, 77, 70, 69, 51, 69, 67, 64, 73, 46, 87, 79, 43, 51, 58, 44, 85, 78, 80, 69, 32, 49, 63, 56, 57, 53, 89, 56]
#for _ in range(50):
 #   random_element = np.random.choice(ages_frequencies)  # Randomly select an element
  #  sample.append(random_element)  # Add the random element to the sublist
#print(ages_frequencies)
print("Sample:",sample)
sample_std = np.std(sample)
sample_mean = np.mean(sample)
print("Sample Mean", sample_mean)
print("Sample STD", sample_std)
plt.hist(sample)
plt.show()
critical_value = norm.ppf(1-(1-.95)/2)
print(critical_value)
m_err = critical_value * (sample_std/math.sqrt(len(sample)))
print(m_err)
lower_bound = sample_mean - m_err
upper_bound = sample_mean + m_err
print(lower_bound, upper_bound)
print("Difference", upper_bound - lower_bound)
std_lower = sample_std - m_err
std_upper = sample_std + m_err
print(std_lower, std_upper)