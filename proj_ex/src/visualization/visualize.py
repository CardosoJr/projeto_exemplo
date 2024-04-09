import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
from plotly import tools

def create_histogram(df, name, color, log = False):
    if name is None:
        data = df.copy()
    else:
        data = df[df['Regionname'] == name].copy()

    if log:
        data['Price'] = np.log(data['Price'])
    

    hist = go.Histogram(
        x = data['Price'].values,
        histnorm = "percent",
        name = f'Price Histogram {name}',
        marker = {'color' : color}
    )

    mean_price = data['Price'].mean()
    line = go.Scatter(
        x = [mean_price, mean_price],
        y = [0, 5],
        mode = 'lines',
        name = f'Mean Price {name}',
        line = {"color" : "#F08CAE",
                "dash" : "dash"
        }
    )
    return hist, line

def plot_histograms(df):
    df['Regionname'].unique()
    COLORS = ['#0101B2', '#B9D6F2', '#F9FBB2', '#7C6354', '#090C08', '#757083', '#8A95A5', '#B9C6AE']
    REGION_COLOR = dict(zip(df['Regionname'].unique(), COLORS))

    region_plot = []

    for region, color in REGION_COLOR.items():
        region_plot.append(create_histogram(df, region, color))

    overall_price = create_histogram(df, None, "#0101B2")
    overall_log_price = create_histogram(df, None, "#0101B2", log = True)

    suptitles = ['Overall'] + list(df['Regionname'].unique()) + ['Log Prices']

    fig = tools.make_subplots(rows = 6, 
                            cols = 2, 
                            subplot_titles = suptitles,
                            specs = [[{'colspan': 2}, None], [{}, {}], [{}, {}], [{}, {}], [{}, {}], [{'colspan': 2}, None]])


    fig.add_traces(overall_price, 1, 1)
    fig.add_traces(region_plot[0], 2, 1)
    fig.add_traces(region_plot[1], 2, 2)
    fig.add_traces(region_plot[2], 3, 1)
    fig.add_traces(region_plot[3], 3, 2)
    fig.add_traces(region_plot[4], 4, 1)
    fig.add_traces(region_plot[5], 4, 2)
    fig.add_traces(region_plot[6], 5, 1)
    fig.add_traces(region_plot[7], 5, 2)
    fig.add_traces(overall_log_price, 6, 1)

    fig.update_layout(title = "Price distribution in Melbourne", height = 1400, width = 900, showlegend = False)

    return fig

