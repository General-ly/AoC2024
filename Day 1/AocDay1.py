import pandas as pd

# Load CSV into DataFrame
cols = ['col_a', 'col_b']
df = pd.read_csv('AocDay1Lists.csv', names=cols, header=None)

# Correctly set column names
df.columns = cols

# Display initial columns
print(df.columns)

# Sort by columns 'col_a' and 'col_b' (sort rows, axis=0 is default)
df = df.sort_values(by=['col_a', 'col_b'], ascending=True)

# If columns are not equal in size, it will throw an error (handled properly here)
try:
    # Check if lengths of columns 'col_a' and 'col_b' are not equal
    if len(df['col_a']) != len(df['col_b']):
        raise ValueError("Columns 'col_a' and 'col_b' are of different lengths.")
except ValueError as e:
    print(f"Error: {e}")
    # Add new column 'col_c' as sum of 'col_a' and 'col_b'
    df['col_c'] = df['col_a'] + df['col_b']
    result = df['col_c'].sum()
    print(result)

# Print final DataFrame

print(df)