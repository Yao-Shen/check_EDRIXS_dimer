import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from IPython.display import display_html

def table(data, sort=None, ascending=False, caption='', disp=True, filename=None, select=None):
    """
    Display the HTML representation of data in form of table.
    
    Parameters
    ----------
    data :  dict,
        Containing all the data to be shown.
    sort :  string,
        Name or list of names to sort by (default: None).
    ascending :  bool or list of bool,
        Sort ascending vs. descending. Specify list for multiple sort
        orders.  If this is a list of bools, must match the length of
        the by. (default: False)
    caption :  string,
        caption for the table (default: '').
    disp :  bool,
        Whether to display the table (default: True).
    filename :  string,
        If given, save the table (default: None).
    select :  int,
        The number of rows to show. If None, all the data will be shown (default: None).
    
    Example
    -------
    >>> summary = dict(Name=['Rick','Morty'], Madness=[100,100])
    >>> table(summary)
    """
    if select is None:
        info = pd.DataFrame(data=np.vstack([data[key] for key in data.keys()]).T, columns=data.keys())
    else:
        info = pd.DataFrame(data=np.vstack([data[key][:select] for key in data.keys()]).T, columns=data.keys())
    
    if sort is not None:
        info = info.sort_values(sort, ascending=ascending)
    
    if filename is not None:
        info.to_csv(filename)
    
    if disp:
        info_styler = info.style.set_table_attributes("style='display:inline'").set_caption(caption)
        display_html(info_styler._repr_html_(), raw=True)

def make_theme(ax, grid=False, gridcolor='gray', gridlw=0.5, logx=False, logy=False, minorx=True, minory=True, ticklength=6, lw=0.5):
    """ Apply the theme for figures """
    if logx:
        ax.set_xscale('log')
        minorx = False
    if minorx:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    if logy:
        ax.set_yscale('log')
        minory = False
    if minory:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    if grid:
        ax.grid(ls=grid, color=gridcolor, lw=gridlw)
    ax.tick_params(which='major', direction='in', left=True, bottom=True, top=True, right=True, width=lw, length=ticklength)
    ax.tick_params(which='minor', direction='in', left=minory, bottom=minorx, top=minorx, right=minory, width=lw, length=ticklength/2)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(lw)