import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

freeE_1 = pd.read_csv("freeE.csv", sep=" ", names=["rmsd1", "freeE"])
freeE_1["rmsd1"] = freeE_1.rmsd1.astype(float)
freeE_1["freeE"] = freeE_1.freeE.astype(float)
kbT = 1.9857831*10**-3*300
beta = (-1.0)/kbT
#print(type(beta))

#print(freeE_1["freeE"].dtype)
freeE_1["power"]=freeE_1["freeE"]*beta
freeE_1["expo"]=np.exp(freeE_1["power"])
normalization_param = freeE_1["expo"].sum()
freeE_1["probability"] = freeE_1["expo"]/normalization_param
freeE_1["rmsd-probability"] = freeE_1["rmsd1"]*freeE_1["probability"]
avg_rmsd = freeE_1["rmsd-probability"].sum()
print(avg_rmsd)

