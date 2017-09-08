import dask.dataframe as dd
import holoviews as hv
from holoviews.operation.datashader import datashade

hv.extension('bokeh')

# 1. Load data and datashade it
df = dd.read_parquet('../data/nyc_taxi_hours.parq/')[['dropoff_x', 'dropoff_y']].persist()
shaded = datashade(hv.Points(df)).opts(plot=dict(width=800, height=600, bgcolor="black"))

# 2. Instead of Jupyter's automatic rich display, render the object as a bokeh document
doc = hv.renderer('bokeh').server_doc(shaded)
doc.title = 'HoloViews Bokeh App'
