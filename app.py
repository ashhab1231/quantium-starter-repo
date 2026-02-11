import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(style={"backgroundColor": "#f4f6f7", "padding": "20px"}, children=[

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "marginBottom": "30px"
        }
    ),

    html.Div([
        html.Label("Select Region:", style={"fontSize": "18px", "fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),
    ], style={"textAlign": "center"}),

    dcc.Graph(id="sales-chart")
])


# Callback to update chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    filtered_df = filtered_df.sort_values("Date")

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Sales": "Total Sales", "Date": "Date"},
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
        title_x=0.5
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
