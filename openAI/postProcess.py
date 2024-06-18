import glob
import pandas as pd

# find all CSV files in the current directory
csv_files = glob.glob('processed/csvs/*.csv')

# create a list to store the dataframes
dfs = []

# loop through the CSV files and read them into dataframes
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# concatenate the dataframes into one dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# write the combined dataframe to a CSV file
combined_df.to_csv('combined.csv', index=False)