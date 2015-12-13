# data coming from https://www.ssa.gov/oact/babynames/limits.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root = "../data/names/"
cols = ["name", "sex", "births"]

names1880 = pd.read_csv(root + 'yob1880.txt', names=cols)
print
print "How many children born in 1880"
print names1880.groupby('sex').births.sum()

# 2015 excluded
years = range(1880, 2015)
pieces = []
for year in years:
    path = root + ('yob%d.txt' % year)
    frame = pd.read_csv(path, names=cols)
    frame['year'] = year
    pieces.append(frame)
# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
print
print "How many were born at this year"
print total_births.tail()

# Insert a column prop with the fraction of babies given each name relative to
# the total number of births. A prop value of 0.02 would indicate that 2 out of every 100
# babies was given a particular name.
def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)
print "Persentage of chidren getting certain name (current context: propagation)"
print names[:10]
print "Check that sum of prop numbers is close to 1"
print np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

# top 1000 names for each year and sex:
pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
# among boys
boys = top1000[top1000.sex == 'M']
# among girls
girls = top1000[top1000.sex == 'F']

# table of births (no sex involved)
total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

plt.show()
