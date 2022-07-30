import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pose_score_pose_1.dat", sep=" ", names=["Trial", "pose1"])
for i in range(2,15):
    df1 = pd.read_csv("pose_score_pose_%s.dat" % i, sep=" ", names=["Trial", "pose%s" % i])
    df = df.merge(df1, on="Trial")

print(df)

pers_score = [0.533, 0.639, 0.582, 0.977, 0.506, 0.382, 0.891, 0.442, 0.650, 0.688, 0.648, 0.642, 1.545, 0.645]
for k in range(1,15):
    df["pose%s" % k] = df["pose%s" % k]-(5*pers_score[k-1])

print(df)

df1 = df.drop("Trial", axis=1)
print(df1)

ax=sns.boxplot(data=df1)
ax.set_ylabel('Comp_Score', fontsize=18)
ax.set_xlabel('Poses', fontsize=18)
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

plt.tight_layout()
#plt.show()
plt.savefig('comp_score_boxplot_AS45_a.png')


