import pandas as pd

df = pd.read_csv("log.csv", parse_dates=[0])

print(df)