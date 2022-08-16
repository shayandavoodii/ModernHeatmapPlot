
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ModernHeatmapPlot(data:pd.DataFrame, x_label:str, y_label:str, legend_label:str="Value", palette=None, save:bool=False):
    """
    Draw a modern Heatmap plot utilizing Seaborn

    Params

    ------

        data:
            A 2-D pandas DataFrame with any shape

        x_label:
            The label of the x axis 

        y_label:
            The label of the y axis 

        legend_label: default="Value"
            Header of legend 

        palette: default=None
            A seaborn palette to change the colormap

        save: default=False
            Save the fig in the current directory

    
    Returns

    -------
    
    None
    """
    data.index.name = 'Ticker'
    df_long = data.reset_index().melt(id_vars='Ticker', var_name='Ticker2', value_name=legend_label)

    if not palette:
        palette = sns.color_palette("coolwarm", as_cmap=True)

    sns.set_style('darkgrid')

    g = sns.relplot(data=df_long,
                    x="Ticker2",
                    y="Ticker",
                    size=legend_label,
                    hue=legend_label,
                    marker="s",
                    sizes=(20, 100),
                    palette=palette,
                    height=8,
                    aspect=1.1
    )

    g.ax.tick_params(axis='x', labelrotation=45)
    g.ax.set_aspect("equal", share=True)
    
    g.fig.set_size_inches(8,8)
    
    # sns.move_legend(g, "lower center",bbox_to_anchor=(0.78, 0.5), title='Bin', frameon=False,)
    
    g.set_xlabels(x_label)
    g.set_ylabels(y_label)
    g.ax.set_facecolor('white')
    g.ax.grid(color='black', lw=0.45)
    g.fig.subplots_adjust(left=0.1, bottom=0.15)
    
    g.savefig("plot.jpeg", dpi=300)
    
    plt.show()