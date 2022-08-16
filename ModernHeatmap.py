import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ModernHeatmapPlot(data:pd.DataFrame, save:bool=False, **kwargs):
    """
    Draw a modern Heatmap plot utilizing Seaborn

    Params

    ------

        data:
            A 2-D pandas DataFrame with any shape

        save: default=False
            Save the fig in the current directory

        kwargs:

            x_label: default="x tickers"
                The label of the x axis 

            y_label: default="y tickers"
                The label of the y axis 

            legend_label: default="Value"
                Header of legend 

            title: String | default=None
                Title of the plot

            palette: default=None
                A seaborn palette to change the colormap
                
    
    Returns

    -------
    
    None
    """
    options = {"x_label":"x tickers", "y_label":"y tickers", "legend_label":"Value", "title":None, "palette":sns.color_palette("coolwarm", as_cmap=True)}
    if kwargs:
        options |= kwargs

    data.index.name = 'Ticker'
    df_long = data.reset_index().melt(id_vars='Ticker', var_name='Ticker2', value_name=options["legend_label"])

    sns.set_style('darkgrid')

    g = sns.relplot(data=df_long,
                    x="Ticker2",
                    y="Ticker",
                    size=options["legend_label"],
                    hue=options["legend_label"],
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
    
    g.set_xlabels(options["x_label"])
    g.set_ylabels(options["y_label"])
    g.ax.set_facecolor('white')
    g.ax.grid(color='black', lw=0.45)
    g.fig.subplots_adjust(left=0.1, bottom=0.15)
    
    if options["title"]:
        plt.title(options["title"])
    
    if save:
        g.savefig(f"fig {options['title']}.jpeg", dpi=300)
    
    plt.show()
