# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import database as db
import matplotlib.pyplot as plt

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

data = db.getTestData()

info1 = data[0]
info2 = data[1]

print(str(info1[0],'utf-8'))

info1Data = [float(str(i,'utf-8').split(":")[0]) for i in info1]
info1Time = [float(str(i,'utf-8').split(":")[1]) for i in info1]

print(info1Data)


df = pd.DataFrame({
    "Time": info1Time,
    "Data": info1Data
})

fig = px.line(df, x="Time", y="Data", title='A Line Plot')


# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.layout = html.Div(children=[
    html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)