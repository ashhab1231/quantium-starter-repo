import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert Date column and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Sales": "Total Sales", "Date": "Date"}
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Dashboard", style={"textAlign": "center"}),

    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)
