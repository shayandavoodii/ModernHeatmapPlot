# <p align="Center">Modern Heatmap Plot</p>
<div  align="center">
<a href="https://t.me/shayandavoodii"><img src="https://badgen.net/badge/icon/Telegram?icon=telegram&label"/></a>
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/shayandavoodii/ModernHeatmapPlot">
</div>

<p align="justify">
Seaborn has become one of the most popular visualization tools in Python. There are numerous variations of charts, which you can organize using Seaborn. Recently, heatmap plots have become one of the most popular types of visual representation. In this repository, I tried to create a modern style (under the guidance of a kind man named Johan. C) by imitating a chart style I've recently seen on Twitter. This plot can be applied to almost any tabular data incorporating various shapes. In the following sections, I'll provide two examples to show the use case of such a plot in Python.
</p>

## First Example
<p align="justify">
Statistics and Almost every Data Scientist utilize special gauges to determine the relationship between variables over time, like Pearson correlation, Spearman's rank correlation, Constant Conditional Correlation (CCC), Dynamic Conditional Correlation, etcetera. In this example, I'll investigate the relation between several synthetic features and depict it using a modern heatmap plot.
</p>

<details>
  <summary>Code</summary>
  
  ```python
  import pandas as pd
  import numpy as np

  np.random.seed(8)

  # Generating synthetic data
  synthetic = np.array([np.random.normal(i, j, 100) for (i,j) in [(0,1), (0,1.5), (-1, 2), (5,7), (2, 9), (8, 8), (15, 15), (6, 30)]])

  # Making some of them a little bit correlated
  synthetic[7] = synthetic[3] + (10 * np.random.randn(100) + 20)
  synthetic[4] = synthetic[3] + (10 * np.random.randn(100) + 10)

  # Sunthetic variable names
  varNames = [f"var{_}" for _ in range(1, synthetic.shape[0]+1)]

  # Creating a pandas DataFrame
  df = pd.DataFrame(synthetic.T, columns=varNames)

  # Storing the correlations
  correlations = df.corr()
  
  options = {"x_label":"Variables", "y_label":"Variables", "legend_label":"Correlation"}
  
  # Drawing the plot using the 'ModernHeatmapPlot' function.
  ModernHeatmapPlot(correlations, **options)
  ```
</details>

The code will result in a modern heatmap plot like this:  
![example1](https://user-images.githubusercontent.com/52105833/184830041-19c1f840-d397-4059-aa33-cb9ce617b939.jpeg)

---

## Second Example
<p align="justify">
Probably you have heard of Bin matrixes. It is possible to produce bin matrices by preprocessing data into small intervals using a data bucket technique. I will also illustrate a Bin matrix using the modern heatmap plot and a conventional heatmap plot so you can distinguish their differences in terms of visualization.
</p>

<details>
  <summary>Code of the modern Heatmap plot</summary>
  
  ```python
  import pandas as pd
  
  df = pd.read_pickle("bindata.pkl")
  
  palette = sns.diverging_palette(145, 300, s=70, as_cmap=True)
  options = {"x_label":"Features", "y_label":"Tickers", "palette":palette, "legend_label":"Bin"}
  
  ModernHeatmapPlot(data=df, **options)
  ```
</details>
Here you can see the difference between these two plots:  

![collage (5)1](https://user-images.githubusercontent.com/52105833/184839462-76e02893-50ef-4ef8-90cc-fdc5bb70491c.jpg)
And if you're interested in high-quality images, unfold the lower section.

<details>
  <summary>Hight quality images</summary>

  ![example2-2](https://user-images.githubusercontent.com/52105833/184839952-7f30afec-22f4-4deb-b927-bd585ecf51af.jpeg)
  ![example2-15](https://user-images.githubusercontent.com/52105833/184839974-61cb2fdb-0250-4386-ac81-230189245063.jpeg)

</details>

---

## Suggestions
Feel free to reach out if you have any suggestions or find any problems with the code. Also, I'll appreciate any contribution to making better plot(s); So any PRs would be warmly welcome.
- <a href="www.linkedin.com/in/shayandavoodi">LinkedIn</a>
- <a href="https://t.me/shayandavoodii">Telegram</a>
---

## Acknowledgements
- I appreciate Johan. C. for his kind attitude towards guiding me in many aspects of drawing the plot.
- Also, I would like to thank my Brazilian friend, [0xAFF](https://github.com/0xAFF), for intuitively proposing cool ideas to draw plots.
