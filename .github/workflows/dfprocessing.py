import pandas as pd

# Create a dictionary with column data
data = {
    'Name': ['John', 'Emma', 'Michael'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)

# Display the dataframe
print(df)
