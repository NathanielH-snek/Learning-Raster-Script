import seaborn as sns
import statannotations as stat
from statannotations.Annotator import Annotator
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stat
import numpy as np

#Read data file and divide into graph groups by list
data = pd.read_excel(io="/Users/11nho/Documents/Learning Study/RatListForSeaborn.xlsx")
df = data.dropna()
data2 = pd.read_excel(io="/Users/11nho/Documents/Learning Study/Cohort6ListforSeaborn.xlsx")
df2 = data2.dropna()

allpairedrats = np.array([1,2,5,6,7,8,15,16,17,19,21,27,31,32,43,52])
allunpairedrats = np.array([47,34,18,17,16,15,14,13,11,9,8,5,4,2,1])
recentpairedrats = np.array([16,15,52])
recentunpairedrats = np.array([18,34,17])

allpairedstats = stat.describe(allpairedrats)
allunpairedstats = stat.describe(allunpairedrats)
recentpairedstats = stat.describe(recentpairedrats)
recentunpairedstats = stat.describe(recentunpairedrats)

summarystats = [allpairedstats,allunpairedstats,recentpairedstats,recentunpairedstats]

for index, stats in enumerate(summarystats):
    print(index, stats)

allratstats = stat.ttest_ind(allpairedrats,allunpairedrats, equal_var=False)
recentratstats = stat.ttest_ind(recentpairedrats,recentunpairedrats, equal_var=False)

ttests = [allratstats, recentratstats]
    
for index, stats in enumerate(ttests):
    print(index, stats)

tvalueallrats = 0.9457556358829634
tvaluerecentrats = 0.3493455899541648
pvalueallrats = 0.3522183714508008
pvaluerecentrats = 0.7515472014920705
#Peform statistical tests on data and save results

#Parameters for statannotations

#Make Graph
order = ['Paired' , 'Unpaired']
pair = [('Paired' , 'Unpaired')]
ax = sns.barplot(data=df2, x="Rat" , y="Nosepokes" , hue="Group" , hue_order=order)
#ax = sns.barplot(data=df, x="Nosepokes" , y="Rat" , hue="Group" , hue_order=order)
#annotator = Annotator(ax, pairs=pair, data=df2, x="Group" , y="Nosepokes")
#annotator.configure(test="t-test_welch", text_format='star', loc='outside')
#annotator.apply_and_annotate()
plt.title('Recent Rats (73-78)')
plt.show()

