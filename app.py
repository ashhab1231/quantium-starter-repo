from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv("formatted_sales_data.csv")

# Fix column name (capital D)
df["Date"] = pd.to_datetime(df["Date"])


app = Dash(__name__)

app.layout = html.Div([

    html.H1("Pink Morsel Sales Visualiser", id="header"),

    dcc.RadioItems(
        id="region-picker",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-graph")
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(region):
    if region != "all":
        filtered = df[df["Region"].str.lower() == region]
    else:
        filtered = df

    fig = px.line(
        filtered.sort_values("Date"),
        x="Date",
        y="Sales",
        title="Sales Over Time"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
