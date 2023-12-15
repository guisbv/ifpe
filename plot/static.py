from data.download import download_data
from plotnine import (
    ggplot, aes,
    geom_line,
    ggtitle,
    xlab, ylab
)

def plot_line(ticker:str) -> ggplot:
    """ Download data from Yahoo Finance

    Args:
        ticker (str): The thicker of financial asset.

    Returns:
        pd.DataFrame: A dataframe retrivied from Yahoo Finance.
    """
    data = download_data(ticker)

    fig = ggplot(
        data = data.reset_index(),
        mapping = aes(x= 'Date', y = 'Close')
    ) + \
        geom_line() + \
        ggtitle('Dados Históricos do {ticker}') + \
        xlab('Data') + \
        ylab('Fechamento')

    return fig