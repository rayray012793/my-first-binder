import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("https://raw.githubusercontent.com/rayray012793/my-first-binder/refs/heads/main/regression_plot.csv")
df_select = df.loc[df.cyl.isin([4, 8]), :]

# 2. Setup Plot Style
sns.set_style("white")

# 3. Create Plot (Robust set to False to avoid RuntimeError)
gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select, 
                     height=7, aspect=1.6, robust=False, palette='tab10', 
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# 4. Customizing Labels for Converter Context
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 55), 
            xlabel='Converter Operating Load (kW)', 
            ylabel='Performance Efficiency (%)')

plt.title("Thermal Efficiency: Load vs. Performance by Cooling Architecture", fontsize=20)
plt.show()
