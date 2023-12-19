# load libraries
import pandas as pd 
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# load dataset
df = pd.read_excel("C:\\Users\\graem\\OneDrive\\Desktop\golf_stats_analysis\\golf_stats_over_time.xlsx") 



# iterate over each seaon and perform ANOVA for DDIS
for season in df['SEASON'].unique():
    df_season = df[df['SEASON'] == season]
    
    formula = 'CUTS ~ DDIS'
    model_anova = ols(formula, data=df_season).fit()
    anova_results = anova_lm(model_anova)

    print(f"\nANOVA results for ddis in the {season} season:")
    print(anova_results)



# iterate over each seaon and perform ANOVA for DACC
for season in df['SEASON'].unique():
    df_season = df[df['SEASON'] == season]
    
    formula = 'CUTS ~ DACC'
    model_anova = ols(formula, data=df_season).fit()
    anova_results = anova_lm(model_anova)

    print(f"\nANOVA results for dacc in the {season} season:")
    print(anova_results)


# iterate over each seaon and perform ANOVA for GIR
for season in df['SEASON'].unique():
    df_season = df[df['SEASON'] == season]
    
    formula = 'CUTS ~ GIR'
    model_anova = ols(formula, data=df_season).fit()
    anova_results = anova_lm(model_anova)

    print(f"\nANOVA results for gir in the {season} season:")
    print(anova_results)


# iterate over each seaon and perform ANOVA for PUTTS
for season in df['SEASON'].unique():
    df_season = df[df['SEASON'] == season]
    
    formula = 'CUTS ~ PUTTS'
    model_anova = ols(formula, data=df_season).fit()
    anova_results = anova_lm(model_anova)

    print(f"\nANOVA results for putts in the {season} season:")
    print(anova_results)
