import pandas as pd

movies = pd.read_csv("IMDB_sample.csv")
print(movies.head())

# Find the number of positive and negative reviews
print("Number of positive and negative reviews: ", movies.label.value_counts())

# Find the proportion of positive and negative reviews
print(
    "Proportion of positive and negative reviews: ",
    movies.label.value_counts() / len(movies),
)
