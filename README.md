Performance visualization
=========================

This is a very simple and short lab to visualize performance metrics of a system. In contrast to previous labs, it focuses on visualizing not only the mean values but also percentiles and the distribution of a metric.

The learning goals of this lab are:

- to plot performance metrics such as mean values, percentiles, and distributions.

> [!NOTE]
> No report is required for this lab.


Files
-----

The following files are already provides:

- `models/simpy_m_m_c.py`: Simple M/M/c queue simulation using the `SimPy` library.
- `visualizations/performance_plots.py`: Functions to create the different plots.
- `./main_mmc.py`: Main file to run a simple M/M/c queue simulation and create the different plots.

Run the simulation
------------------

Simply run the `main_mmc.py` file to run a simple M/M/c queue simulation and create the different plots:

It will generate the following plots:

- `scatter.png`: Scatter plot of the response times.
- `histogram.png`: Histogram of the response times.
- `percentiles.png`: Percentile plot of the response times.
- `heatmap.png`: Heatmap plot of the response times.

Interpret the plots
-------------------

Look at each of the for plots. 

- What information is shown in each plot?
- What are the advantages and disadvantages of each plot?
- When would you use which plot?
