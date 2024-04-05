import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, None, 4]})

# Detecting nulls
nulls = df.isnull()
print(nulls)
