# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 02:50:51 2025

@author: Ignite Capital
"""

import numpy as np
import matplotlib.pyplot as plt
filename = "data.csv"


data = [10,20,30,40,50,60,70,80,90,100]

mean_value = np.mean(data)
variance_value = np.var(data)
std_deviation = np.std(data)
print(f"Mean: {mean_value}\n")
print(f"Variance: {variance_value}\n")
print(f"Standard Deviation: {std_deviation}\n")
plt.hist(data, bins=5, color='blue', alpha=0.7)
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt. title("Histogram of Sampe Data")
plt.show()
