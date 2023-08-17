#https://www.nobelprize.org/prizes/lists/nobel-laureates-by-age/
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

mean = np.mean(ages_frequencies)
median = np.mean(ages_frequencies)
mode = st.multimode(ages_frequencies)
std_dev = np.std(ages_frequencies)
print("Mean : ", mean)
print("Median : ",median)
print("SD : ",std_dev)
print("Mode", mode)

# Define the standard deviation ranges

std_ranges = [1, 2, 3,4]
colors = ["","#3e4444","#82b74b","#405d27","#c1946a"]
# Create a histogram
plt.hist(ages_frequencies, alpha=1, color='blue')

probd = 0 # Prob difference
for std in std_ranges:
    upper_bound = mean + std_dev * std
    lower_bound = mean - std_dev * std


    # Color the segment between lower and upper bounds
    plt.axvspan(lower_bound, upper_bound, color=colors[std], alpha=0.3)
    #Probabalities within stds
    prob = (norm.cdf(upper_bound, loc=mean, scale=std_dev) - norm.cdf(lower_bound, loc=mean, scale=std_dev))*100
    #Probs within (m +- nSTDs)
    quart_prob = (prob-probd)/2
    probd = prob
    print(f"Probability within {std} standard deviations: {prob:.2f}")
    prob_t =f"{(quart_prob):.2f}%"
    plt.axvline(lower_bound, color=colors[std], linestyle=":")
    plt.axvline(upper_bound, color=colors[std], linestyle=":")
    plt.annotate(prob_t, xy=(lower_bound, 100))
    plt.annotate(prob_t, xy=(upper_bound-10, 100))
    ypoint = 10*std
    plt.plot([lower_bound, upper_bound], [ypoint, ypoint], color=colors[std], linestyle='-', label='Line')


    plt.annotate(f"{prob:.2f}%", xy=(lower_bound+5, ypoint), ha='center', color=colors[std], fontsize=14)

#working



#working


plt.axvline(mean,  color="black", linestyle="--")
plt.xlabel('Ages')
plt.ylabel('Winners')
plt.title('Noble Prize Winners VS Age')
plt.xticks(np.arange(10,100,5))
plt.show()
# End of program