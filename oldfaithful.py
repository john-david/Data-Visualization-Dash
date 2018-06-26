
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("OldFaithful.csv")

# print(df.head)

app = dash.Dash()

server = app.server

app.layout = html.Div([dcc.Graph(id = 'old_faithful',
                                 figure = {'data' : [go.Scatter(x = df['X'],
                                                                y = df['Y'],
                                                                mode = 'markers')],

                                 'layout' : go.Layout(
                                    title = 'Old Faither Eruptions',
                                    xaxis = {'title': 'Duration of eruption (minutes)'  },
                                    yaxis = {'title': 'Interval to next eruption (minutes)'  },
                                    hovermode = 'closest'
                                    )

                                 })
                        ])

if __name__ == '__main__':
    app.run_server()
