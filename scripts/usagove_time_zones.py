
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
import json

# data came from
# https://github.com/usagov/1.USA.gov-Data
# it streams data into the file. should wait for a while to get more data

data_path = '../data/usagov.json'
records = [json.loads(line) for line in open(data_path)]
frame = DataFrame(records)


tz_counts = frame['tz'].value_counts()
print "Count of top 10 values tz without NA:"
print tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
print
print "Count of missing tz values:"
print clean_tz[clean_tz == 'Missing'].count()

clean_tz[clean_tz == ''] = 'Unknown'
print
print "Count of empty tz values:"
print clean_tz[clean_tz == 'Unknown'].count()

# draw graph that shows how many people from top 10 tz
tz_counts[:10].plot(kind='barh', rot=0, title="Top 10 values tz counts")

# where we have browser string
cframe = frame[frame.a.notnull()]
# creating new column with os only
cframe['os'] = Series(np.chararray(cframe.a.shape))
cframe.os[:] = 'Not Windows'
cframe.os[cframe.a.str.contains('Windows')] = 'Windows'

# grouping by time zones and os
by_tz_os = cframe.groupby(['tz', 'os'])
# for each group we find how many elements in the group
by_tz_os = by_tz_os.size()
print
print "Count of users who have particular tz and os"
print by_tz_os[:10]

print
print "Pivoting last column and putting 0 where no os in tz"
# by default last level
by_tz_os = by_tz_os.unstack()
by_tz_os = by_tz_os.fillna(0)
print by_tz_os[:10]

# sum columns and sorting, extract sorted indices
indexer = by_tz_os.sum(1).argsort()
# take from end
count_subset = by_tz_os.take(indexer)[-10:]#[::-1] doesn't work for graphs
count_subset.reindex(index=count_subset.index[::-1])
print
print "Top 10 tz and os"
print count_subset

count_subset.plot(kind='barh', stacked=True, title='Top 10 tz and os')
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True, title='Top 10 tz and os normalized by count')

plt.show()
