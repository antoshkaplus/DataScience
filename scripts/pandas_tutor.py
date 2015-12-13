import pandas as pd

### Series ###

# Series - array of data (behaives like map a bit)
# can do vector operations
obj = Series([4, 7, -5, 3])
print obj.values
print obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print obj2.index
print 'b' in obj2
print 'e' in obj2

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
# some stuff is out California is NaN

# isnull and notnull functions in pandas should be used to
# detect missing data
print pd.isnull(obj4)
print pd.notnull(obj4)

# automatically aligns differently indexed
# data in arithmetic operations

obj4.name = 'population'
obj4.index.name = 'state'

# Series index can be altered in place by assignment
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

### DataFrame ###

# has both a row and column index
# it can be thought of as a dict of Series (one for all sharing the same index).

# Under the hood, the data is stored as one or more two-dimensional blocks rather
# than a list, dict, or some other collection of one-dimensional arrays. The exact details
# of DataFrame’s internals are far outside the scope of this book.

# ways to construct
# dict of equal length lists
data = {
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

frame = DataFrame(data)
# can specify sequence of colunms
frame = DataFrame(data, columns=['year', 'state', 'pop'])
# if don't have column in data NaN values would be the case

# Returned Series have the same index as the DataFrame, and their name
# attribute has been appropriately set.

# Rows can also be retrieved by position or name by a couple of methods, such as the
# ix indexing field
frame2.ix['three']

# Assigning a column that doesn’t exist will create a new column. The del keyword will
# delete columns as with a dict


### Index ###

# responsible for holding the axis labels and other metadata
# (like the axis name or names)
# Index objects are immutable
