# load libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# load dataset
df = pd.read_excel("C:\\Users\\graem\\OneDrive\\Desktop\golf_stats_analysis\\golf_stats_over_time.xlsx") 

# select data for Scottie Scheffler and Nate Lashley in the 2022-2023 season
scottie_data = df[(df['NAME'] == 'Scottie Scheffler') & (df['SEASON'] == '2022-2023')]
nate_data = df[(df['NAME'] == 'Nate Lashley') & (df['SEASON'] == '2022-2023')]

variables = ['DDIS', 'DACC', 'GIR', 'PUTTS']

# Set up bar plots
plt.figure(figsize=(12, 8))

# loop through variables and create grouped bar plots
for i, variable in enumerate(variables):
    plt.subplot(2, 2, i+1)
    
   
    if variable == 'DDIS':
        sns.barplot(x='NAME', y=variable, data=pd.concat([scottie_data, nate_data]), palette='viridis', ci=None)
        plt.ylim(250, max(df[variable]))  # Set y-axis limit for 'DDIS'
    elif variable == 'GIR':
        sns.barplot(x='NAME', y=variable, data=pd.concat([scottie_data, nate_data]), palette='viridis', ci=None)
        plt.ylim(60, 76)  # Set y-axis limit for 'GIR'
    elif variable == 'DACC':
        sns.barplot(x='NAME', y=variable, data=pd.concat([scottie_data, nate_data]), palette='viridis', ci=None)
        plt.ylim(40, max(df[variable]))  # Set y-axis limit for 'DACC'
    elif variable == 'PUTTS':
        sns.barplot(x='NAME', y=variable, data=pd.concat([scottie_data, nate_data]), palette='viridis', ci=None)
        plt.ylim(1.00, max(df[variable]))  # Set y-axis limit for 'DACC'
    else:
        sns.barplot(x='NAME', y=variable, data=pd.concat([scottie_data, nate_data]), palette='viridis', ci=None)
    
    # make labels and titles
    plt.xlabel('')
    plt.ylabel(variable)
    plt.title(f'{variable} Comparison')

plt.tight_layout()
plt.show()
