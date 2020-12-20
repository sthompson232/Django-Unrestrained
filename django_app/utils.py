from matplotlib import pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import base64
from io import BytesIO



def get_prices(data_type, start_date, end_date):
    return web.DataReader(data_type, 'fred', start_date, end_date)


def get_fred_query(data_type, start_date, end_date):
    fred_dataframe = get_prices(data_type, start_date, end_date)
    # print(fred_dataframe)
    # CREATE VARIABLES FOR GRAPH
    x = fred_dataframe.index
    y = fred_dataframe[data_type]
    title = f"Quantity of {data_type} (US)"
    x_label = "Time"
    y_label = f"{data_type} quantity"
    # print(y)
    graph = get_plot(x, y, title, x_label, y_label)
    return graph

# FUNCTION TO ALLOW MATPLOTLIB TO WORK ON DJANGO. THIS IS CALLED IN ALL OF THE OTHER GRAPH FUNCTIONS
# I DO NOT FULLY UNDERSTAND THIS MYSELF!
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, title, x_label, y_label):
    plt.switch_backend('AGG')

    # GRAPH CREATION
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.plot(x,y, color="red")
    plt.xticks(rotation=45)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    graph = get_graph()
    return graph