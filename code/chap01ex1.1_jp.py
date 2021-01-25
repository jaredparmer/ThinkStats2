from __future__ import print_function, division
import nsfg

preg = nsfg.ReadFemPreg()
preg.head()

# print the value counts of the birthord column
print(preg.birthord.value_counts())
print("null values:", preg.birthord.isnull().sum())

# summary of weights
print("mean of totalwgt_lb:", preg.totalwgt_lb.mean())
print("creating new column, totalwgt_kg...")
preg['totalwgt_kg'] = preg.totalwgt_lb / 2.205
print(preg.totalwgt_kg.value_counts())
print("mean of totalwgt_kg:", preg.totalwgt_kg.mean())

resp = nsfg.ReadFemResp()

# print the value counts of the age_r column
print(resp.age_r.value_counts().sort_index())

# fetch some data
print("age of respondent with caseid 1:")
print(resp[resp.caseid==1].age_r)
print("pregnancy lengths of respondent 2298:")
print(preg[preg.caseid==2298].prglngth)
print("birthweight of babies born to respondent 5012:")
print(preg[preg.caseid==5012].birthwgt_lb)
