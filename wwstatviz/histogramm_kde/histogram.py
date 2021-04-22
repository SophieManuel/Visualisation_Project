# %%
# libraries
import csv
from download import download
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact
from wwstatviz import data

# %%
# tables
tab_fert = pd.read_csv("FertilityByAge.csv")
tab_indic = pd.read_csv("Period_Indicator_Medium.csv")
tab_TotPop = pd.read_csv("TotalPopBySex.csv")

# %%
# histogramm exemple incomplet
plt.figure(figsize=(5, 5))
plt.hist(tab_TotPop['Age'], density=True, bins=25)
plt.xlabel('Age')
plt.ylabel('Proportion')
plt.title("Passager age histogram")
# interact
