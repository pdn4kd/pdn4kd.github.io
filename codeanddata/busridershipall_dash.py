'''Putting together a ridership dashboard'''
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
#import matplotlib.pyplot as plt
#import numpy as np

# Initialize the app
app = Dash()

# Incorporate data
data = pd.read_csv('TotalBoardingsPaid.csv')
data1month = pd.read_csv('WMATA202601.csv')

# Setup constants
yoymonth = [1,2,3,4,5,6,7,8,9,10,11,12]
mommonth = [1,2,3,4,5,6,7,8,9,10,11,12]

# App layout
app.layout = [
	html.Div(children='WMATA Metrobus ridership and fare payment examples'),
	html.Hr(),
	dcc.Graph(figure={}, id='YearOverYear', style={'width': '40%'}),
	dcc.Graph(figure={}, id='MonthOverMonth', style={'width': '40%'}),
	dcc.Graph(figure={}, id='TimeSeries', style={'width': '100%'}),
	dcc.RadioItems(options=['Weekday', 'Saturday', 'Sunday', 'Total'], value='Weekday', id='day-of-week'),
	html.Hr(),
	dcc.Graph(figure={}, id='MonthlySnapshot', style={'width': '60%'}),
]

@callback(
	Output(component_id='TimeSeries', component_property='figure'),
	Input(component_id='day-of-week', component_property='value')
)
def update_graph(val_chosen):
	allriders = val_chosen + "Boardings"
	paidriders = val_chosen + "Paid"
	fig = px.bar(data, x='Month', y=[allriders, paidriders], barmode="group", labels={'Month':'Months Since 2018/07', 'value':'Monthly Riders', 'variable':'Rider Type'}, title="Overall Time Series")
	return fig

@callback(
	Output(component_id='YearOverYear', component_property='figure'),
	Input(component_id='day-of-week', component_property='value')
)
def update_graph(val_chosen):
	allriders = val_chosen + "Boardings"
	paidriders = val_chosen + "Paid"
	yoytotal = 100*(data[allriders][-12:].values - data[allriders][-24:-12].values)/data[allriders][-24:-12].values
	yoypaid = 100*(data[paidriders][-12:].values - data[paidriders][-24:-12].values)/data[paidriders][-24:-12].values
	fig = px.bar(title="Year Over Year Change", x=yoymonth, y=[yoytotal, yoypaid], barmode="group", labels={'x':'Month', 'value':'Percent Change vs Previous Year', 'variable':'Rider Type', 'wide_variable_0':'All', 'wide_variable_1':'Paid'})
	return fig

@callback(
	Output(component_id='MonthOverMonth', component_property='figure'),
	Input(component_id='day-of-week', component_property='value')
)
def update_graph(val_chosen):
	allriders = val_chosen + "Boardings"
	paidriders = val_chosen + "Paid"
	momtotal = 100*(data[allriders][-12:].values - data[allriders][-13:-1].values)/data[allriders][-13:-1].values
	mompaid = 100*(data[paidriders][-12:].values - data[paidriders][-13:-1].values)/data[paidriders][-13:-1].values
	fig = px.bar(title="Month Over Month Change", x=mommonth, y=[momtotal, mompaid], barmode="group", labels={'x':'Month', 'value':'Percent Change vs Previous Month', 'variable':'Rider Type', 'wide_variable_0':'All', 'wide_variable_1':'Paid'})
	return fig

# Per-bus ridership
@callback(
	Output(component_id='MonthlySnapshot', component_property='figure'),
	Input(component_id='day-of-week', component_property='value')
)
def update_graph(val_chosen):
	xs = val_chosen + "Boardings"
	ys = val_chosen + "Paid"
	fig = px.scatter(data1month, xs, ys, color="Location", trendline="ols", title="January 20216 Per-Neighborhood Breakdown")
	return fig

if __name__ == '__main__':
	app.run(debug=True)
