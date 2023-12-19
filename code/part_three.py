# load libraries
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel("C:\\Users\\graem\\OneDrive\\Desktop\golf_stats_analysis\\golf_stats_over_time.xlsx") 


# select schefflers data
scottie_data = df[df['NAME'] == 'Scottie Scheffler']

# select variables to compare
key_stats = ['DDIS', 'DACC', 'GIR', 'PUTTS']


# create scatter plots
plt.figure(figsize=(12, 8))

for i, stat in enumerate(key_stats):
    plt.subplot(2, 2, i+1)
    
    
    for season in scottie_data['SEASON'].unique():
        season_data = scottie_data[scottie_data['SEASON'] == season]
        plt.plot(season_data['SEASON'], season_data[stat], marker='o', label=season)

   # add line going through each point
    plt.plot(scottie_data['SEASON'], scottie_data[stat], linestyle='-', linewidth=1, color='black')

    # make labels and title
    plt.xlabel('Season')
    plt.ylabel(stat)
    plt.title(f'{stat} Over Seasons')
    plt.legend()

plt.tight_layout()
plt.show()
