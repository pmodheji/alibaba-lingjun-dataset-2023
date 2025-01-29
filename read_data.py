import pandas as pd

# Read the CSV file from the data subfolder
df = pd.read_csv('data/job.csv')

# Display the first few rows of the dataframe
print(df.head())

# Display 5 random rows for columns 17 to 30 and columns 32 and 33
print(df.iloc[:, list(range(17, 31)) + [32, 33]].sample(5))d