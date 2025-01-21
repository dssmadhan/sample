import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Crop_recommendation.csv')

# Drop a column by name (e.g., 'column_to_drop')
df = df.drop(columns=['label'])

# If you want to drop multiple columns, pass a list of column names
# df = df.drop(columns=['column1', 'column2'])

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_file.csv', index=False)