import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup Theme & Fonts based on your screenshot parameters
params = {'axes.titlesize': 22, 'legend.fontsize': 11, 'figure.figsize': (16, 10),
          'axes.labelsize': 16, 'xtick.labelsize': 12, 'ytick.labelsize': 12}
plt.rcParams.update(params)
sns.set_style("white")
%matplotlib inline

# 2. Load the Dataset
midwest = pd.read_csv("https://github.com/rayray012793/my-first-binder/blob/main/scatterplot2.csv")

# 3. Create Color Palette for the 6 States
states_list = np.unique(midwest['state'])
colors = [plt.cm.tab10(i/float(len(states_list)-1)) for i in range(len(states_list))]

# 4. Draw Dense Bubble Plot
plt.figure(figsize=(16, 10), dpi=100)

for i, state in enumerate(states_list):
    subset = midwest.loc[midwest.state == state, :]
    
    plt.scatter('area', 'poptotal',
                data=subset,
                s='dot_size',
                c=[colors[i]],
                label=state,
                alpha=0.55,      # Transparency to show density/overlap
                edgecolors='white', 
                linewidths=.5)

# 5. Formatting & Industry-Standard Labeling
plt.gca().set(xlim=(0.0, 0.12), ylim=(0, 110000),
              xlabel='Physical Footprint (m^2 normalized)', 
              ylabel='Rated Power Capacity (Watts)')

plt.title("US Regional Power Converter Analysis: Area vs. Power Capacity", fontsize=22)
plt.legend(title="Installed States", loc='upper right', markerscale=0.6)
plt.show()
