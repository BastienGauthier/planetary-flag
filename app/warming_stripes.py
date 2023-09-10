#%%
# Importation
import matplotlib.pyplot as plt

from utils import (
    FIRST,
    LAST,
    FIRST_REFERENCE,
    LAST_REFERENCE,
    get_warming_stripes_cmap
    )

from plot_stripes import get_stripes_collection

from read_data import get_df_temperature_anomaly

#%%
# Parameters
LIM = 0.7 # degrees
N_PLOTS = 1

## Colormap
cmap = get_warming_stripes_cmap()

#%%
anomaly = get_df_temperature_anomaly()
reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()


#%%
# Figure
y0 = 0

fig = plt.figure(figsize=(10, 1))

ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()

# create a collection with a rectangle for each year
col = get_stripes_collection(
    anomaly, 
    cmap, 
    reference - LIM, 
    reference + LIM,
    y0
    )
ax.add_collection(col)

# Correct the axes and save fig
ax.set_ylim(0, N_PLOTS)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('../img/warming-stripes.png')