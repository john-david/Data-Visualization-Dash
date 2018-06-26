
# plotly dashboard

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

server = app.server

# create some data

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id = 'scatterplot',
        figure = {'data':[
                    go.Scatter(
                    x = random_x,
                    y = random_y,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(50, 100, 100)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                    )],
                  'layout': go.Layout(title = 'Random Scatterplot 1',
                                      xaxis = {'title': 'random x'})}

    ), dcc.Graph(id = 'scatterplot2',
        figure = {'data':[
                    go.Scatter(
                    x = random_x,
                    y = random_y,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(150, 50, 50)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                    )],
                  'layout': go.Layout(title = 'Random Scatterplot 2',
                                      xaxis = {'title': 'random x'})}

    )

])

if __name__ == '__main__':
    app.run_server()



