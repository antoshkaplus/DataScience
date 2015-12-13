import pandas as pd

# very popular data set
# currently located here: http://grouplens.org/datasets/movielens/

root = "../data/movie_length-1m/"

# read tables
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(root + 'users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(root + 'ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(root + 'movies.dat', sep='::', header=None, names=mnames)

# going to merge data by looking at the same columns
data = pd.merge(pd.merge(ratings, users), movies)

# mean movie ratings grouped by title and gender, pivot gender
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
print "Mean ratings:"
print mean_ratings[:10]

#  group the data by title and use size() to get a Series of group sizes for each title
ratings_by_title = data.groupby('title').size()
print
print "Movie popularity:"
print ratings_by_title[:10]

# taking indecies of most popular movies
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]

# what women like most
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
print
print "Top female movies"
top_female_ratings[:10]

# the movies that are most divisive between male and female viewers
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
# women like over men
print
print "Women like over men"
print sorted_by_diff[:10]

# men like over women
print
print "Men like over women"
print sorted_by_diff[::-1][:10]


# elicited - vizvalo
# most disagreement independent of gender
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# Order Series by value in descending order
print
print "Most disagreement independent of gender"
print rating_std_by_title.order(ascending=False)[:10]
