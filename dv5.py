import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template



df = pd.read_csv("D:\\College\\data visualization\\dv\\Spotify Top 200 Global (2017-2021).csv")

print(df.head())

load_figure_template("QUARTZ")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
colors = {

    'text': '#008000'
}
app.layout = html.Div([
    html.H1("Songs charts dashboard", style={"textAlign":"center","color":colors["text"]}),
    html.Hr(),
 dbc.Row([
        dbc.Col([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/548.jpg", "img_style":{"height":"400px"} },
                    {"key": "2", "src": "/assets/download.jpg", "img_style":{"height":"400px"}},
                    {"key": "3", "src": "/assets/Dj.jpg", "img_style":{"height":"400px"}},
                    {"key": "4", "src": "/assets/demi.jpg", "img_style":{"height":"400px"}},
                    {"key": "5", "src": "/assets/Divide_cover.png", "img_style":{"height":"400px"}},
                    {"key": "6", "src": "/assets/adele.jpg", "img_style":{"height":"400px"}},
                    {"key": "7", "src": "/assets/ariana.jpg", "img_style":{"height":"400px"}},
                    {"key": "8", "src": "/assets/ava.jpg", "img_style":{"height":"400px"} },
                    {"key": "9", "src": "/assets/camila.jpg", "img_style":{"height":"400px"}},
                    {"key": "10", "src": "/assets/images.jpg", "img_style":{"height":"400px"}},
                    {"key": "11", "src": "/assets/imagine.jpg", "img_style":{"height":"400px"}},
                    {"key": "12", "src": "/assets/katy.jpg", "img_style":{"height":"400px"}},
                    {"key": "13", "src": "/assets/lewis.jpg", "img_style":{"height":"400px"}},
                    {"key": "14", "src": "/assets/marron 5.jpg", "img_style":{"height":"400px"}},
                    {"key": "15", "src": "/assets/martin.jpg", "img_style":{"height":"400px"} },
                    {"key": "16", "src": "/assets/maskedwolf.jpg", "img_style":{"height":"400px"}},
                    {"key": "17", "src": "/assets/miley.jpg", "img_style":{"height":"400px"}},
                    {"key": "18", "src": "/assets/sia.jpg", "img_style":{"height":"400px"}},
                    {"key": "19", "src": "/assets/theweekend.jpg", "img_style":{"height":"400px"}},
                    {"key": "20", "src": "/assets/zayn.jpg", "img_style":{"height":"400px"}},
                    {"key": "21", "src": "/assets/meghan.jpg", "img_style":{"height":"400px"}},
                ],
                controls=False,
                indicators=False,
                interval=2000,
                ride="carousel",
                className="carousel-fade"
            )
        ], width=4)
    ], justify="center"),
    html.P("interested year:"),
    html.Div(html.Div([
        dcc.Dropdown(id='year', clearable=False,
                     value="2019",
                     options=[{'label': x, 'value': x} for x in
                              df["year"].unique()]),
    ],className="two columns"),className="row"),

    html.Div(id="output-div", children=[]),
])


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="year", component_property="value"),
)
def make_graphs(dashboard):
    # HISTOGRAM
    df_hist = df[df["year"]==dashboard]
    fig_hist = px.histogram(df_hist, y="Streams",x="Artist",color="Explicit",color_discrete_sequence=["purple","pink"])
    fig_hist.update_xaxes(categoryorder="total descending")
    fig_scatter = px.scatter(df_hist, x="Duration_MS", y="Artist_Followers",
                     size="Streams",symbol="Explicit", color="Artist",opacity=0.3,
                     hover_data=["Track","Artist","Album_Name"], log_x=True, size_max=60)

    fig_sburst = px.sunburst(df_hist, path=['Explicit','Artist',"Track"],color_discrete_sequence=["pink","purple"],hover_data=["Track_Number_on_Album","Album_Name"])
    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className=" twelve columns"),
            html.Div([dcc.Graph(figure=fig_scatter)], className=" twelve columns"),
            html.Div([dcc.Graph(figure=fig_sburst)], className=" twelve columns"),
        ], className=" row"),

    ]


if __name__ == '__main__':
    app.run_server(debug=True,port=8000)

