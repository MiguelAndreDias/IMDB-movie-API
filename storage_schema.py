import pandas as pd

#Opens the two files containing the relevant IMDB data and turns them into panda dataframes
file_path1 = "title.basics.tsv.gz"
file_path2 = "title.ratings.tsv.gz"
df1 = pd.read_csv(file_path1, sep='\t', compression='gzip')
df2 = pd.read_csv(file_path2, sep='\t', compression='gzip')

#Merges both DF and saves the result into a csv file.
merged_df = df1.merge(df2,how='left', left_on='tconst', right_on='tconst')
merged_df.to_csv('finaldata.csv', sep='\t', index=False, header=True)


#Opens the previously merged DF and selects the rows that contain the movie tag in the titleType column
final = pd.read_csv("finaldata.csv", delimiter ='\t')
final_movies = final[final['titleType'] == 'movie']


#Drops irrelevant columns.
final_movies.drop(columns = ['originalTitle', 'endYear', 'numVotes', 'isAdult'], inplace = True)

#Adds an imdb page link column for every row.
final_movies['imdbLink'] = 'https://www.imdb.com/title/' + final_movies['tconst']

#Saves the modified DF into a new CSV file.
final_movies.to_csv('moviesonly2.csv', sep='\t', index=False, header=True)
print(final_movies.head(10))



""" 
# Count the rows with 'titleType' equal to 'Movie' in both the original and modified dataset.
movie_count = (final['titleType'] == 'movie').sum()

movie_count2 = (final_movies['titleType'] == 'movie').sum()
# Display the count
print(f"Number of rows with 'Movie' tag: {movie_count}")

print(f"Number of rows with 'Movie' tag: {movie_count2}")


 """