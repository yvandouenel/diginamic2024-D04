import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file: df
netflix_df = pd.read_csv('netflix_titles.csv')
recent_release_date = netflix_df[["release_year","title","type"]].groupby(["type"]).max()['title'].tolist()[0]
print(recent_release_date)