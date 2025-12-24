import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# 1. Plot Parameters & Styling
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': small, # Smaller font to fit more states
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
sns.set_style("white") 
%matplotlib inline

# 2. Import high-density dataset 
# Ensure your CSV has 'area', 'poptotal', 'state', 'dot_size'
midwest = pd.read_csv("https://raw.githubusercontent.com/rayray012793/my-first-binder/refs/heads/main/power_data.csv") 

# 3. Prepare Colors based on STATE instead of Category
# This allows you to see the geographic distribution
states_list = np.unique(midwest['state'])
colors = [plt.cm.tab20(i/float(len(states_list)-1)) for i in range(len(states_list))]

# 4. Draw Bubble Plot
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, state in enumerate(states_list):
    data_subset = midwest.loc[midwest.state==state, :]
    
    plt.scatter('area', 'poptotal',
                data=data_subset,
                s='dot_size',      
                c=[colors[i]],     
                label=str(state),  # Legend now shows States (IL, WI, CA, etc.)
                alpha=0.6,         
                edgecolors='white', 
                linewidths=.5)

# 5. Decorations & Axis Setup
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 105000),
              xlabel='Normalized Area', ylabel='Total Population / Usage')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Regional Power Usage Analysis: Area vs Population (by State)", fontsize=22)

# Legend settings
plt.legend(title="States", loc='upper right', markerscale=0.5) 
plt.show()
