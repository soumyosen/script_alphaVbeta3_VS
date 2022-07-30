import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pose_score_pose_1.dat", sep=" ", names=["Trial", "pose1"])
for i in range(2,15):
    df1 = pd.read_csv("pose_score_pose_%s.dat" % i, sep=" ", names=["Trial", "pose%s" % i])
    df = df.merge(df1, on="Trial")

#print(df)

dfT = df.T
dfT.columns = dfT.iloc[0]
dfT_1 = dfT[1:]
#print(dfT_1)

#print(dfT_1.columns)
#print(dfT_1.index)


dfT_1.reset_index(inplace=True)
dfT_2 = dfT_1.rename(columns = {'index':'pose'})
print(dfT_2)
columns = list(dfT_2.columns)
columns.remove("pose")
#print(columns)

dfT_2["Mean"] = dfT_2[columns].mean(axis = 1)
dfT_2["Std"] = dfT_2[columns].std(axis = 1)
print(dfT_2)

fig, ax = plt.subplots(nrows=1, ncols=1)

ax.bar(dfT_2["pose"], dfT_2["Mean"], yerr=dfT_2["Std"], color='green', alpha=0.3, ecolor='black', capsize=3,
        label="With SCD", align='center', width=0.3)
ax.set_ylabel('Average RMSD ($\AA$)', fontsize=18)
ax.set_xlabel('Poses', fontsize=18)
ax.set_xticklabels(dfT_2["pose"], rotation=90, fontsize=12)

fig.tight_layout()
#plt.show()
plt.savefig('pose_score_AS45_a.png')


