# # * Plot stock data that we retrieved using yf or IEXcloud in a candlestick plot using plotly
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('IEXcloudStockOutput.csv')

#print(df)
# * From plotly documentation: https://plotly.com/python/candlestick-charts/
candlestick = go.Candlestick(x=df['date'], # * 'x=' gives x-axis
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])

figure = go.Figure(data=[candlestick]) # * Create figure
#figure.show() # * Shows interactive candlestick plot in browser on local drive
figure.layout.xaxis.type = 'category' # * Adds some formatting

# * Add example shapes and annotations to figure
shapes = [
    dict(x0='2020-09-29', x1='2020-09-29', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2020-10-27', x1='2020-10-27', y0=0, y1=1, xref='x', yref='paper')
]
annotations = [
    dict(x='2020-09-29', y=.9, xref='x', yref='paper', showarrow=False, xanchor='left', text='My Bday'),
    dict(x='2020-10-27', y=.9, xref='x', yref='paper', showarrow=False, xanchor='left', text="Wife's Bday")
]

figure.update_layout(title='INTC Stock Data', annotations=annotations, shapes=shapes) # * Update figure
figure.write_html('intc.html',auto_open=True) # * Creates static HTML file

