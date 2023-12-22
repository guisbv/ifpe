import plotly.express as px
from data.download import download_data

def plot_line_i(ticker:str):

    data = download_data(ticker)

    fig = px.line(
        data.reset_index(),
        x='Date', y='Close', title = ticker,
        labels={'Close': 'fechamento', 'Date': 'Data'}
    )

    return fig