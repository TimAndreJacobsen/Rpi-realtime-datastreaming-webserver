import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("log.csv", parse_dates=[0])

print(df)

html = df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', 
formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, 
classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', 
border=None, table_id=None)

print(html)

N = 500


x = np.linspace(0, 1, N)
y = np.random.randn(N)
df = pd.DataFrame({'x': x, 'y': y})
df.head()

x2 = np.linspace(0, 1, N)
y2 = np.random.randn(N) + 3
df2 = pd.DataFrame({'x': x2, 'y': y2})
df2.head()

data = [
    go.Scatter(
        x=df['x'], # assign x as the dataframe column 'x'
        y=df['y'],
        name='random around 0'
    ),
    go.Scatter(
        x=df2['x'], # assign x as the dataframe column 'x'
        y=df2['y'],
        name='random around 3'
    )
]

url = py.plot(data, filename='pandas-line-naming-traces')