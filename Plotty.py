# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import database.database as database
from RedisTestData import *
from pprint import pprint

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

db = database.build_redis_connection()
device = ["Device1"]
parameters = ["TEMPERATURE","HUMIDITY","PRESSURE","COMPASS"]
rawdataList = {}
for d in device:
    for p in parameters:
        rawdataList[d+":"+p] = rawToTime(readList(d+":"+p,db))
        


df = pd.DataFrame({
    "Time": rawdataList["Device1:HUMIDITY"][1],
    "Data": rawdataList["Device1:HUMIDITY"][0]
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