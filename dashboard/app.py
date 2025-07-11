import dash
from dash import html, dcc, dash_table
import pandas as pd

app = dash.Dash(__name__)
app.title = "Real-Time Fraud Alerts"

def load_alerts():
    try:
        df = pd.read_csv("alerts.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["transaction_id", "amount", "prediction"])
    return df

app.layout = html.Div([
    html.H1("Live Fraud Detection Dashboard"),
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0),
    html.Div(id='live-update-table')
])

@app.callback(
    dash.dependencies.Output('live-update-table', 'children'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_table(n):
    df = load_alerts()
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_table={'overflowX': 'auto'}
    )

if __name__ == '__main__':
    app.run_server(debug=True)
