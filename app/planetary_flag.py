# %%
# Importation
import matplotlib.pyplot as plt

from read_data import (
    get_s_climate_change,
    get_s_ocean_acidification,
    get_s_stratosferic_ozone,
    get_s_atmospheric_aerosol,
    get_s_biogeochimical_phosphore,
    get_s_biogeochimical_nitrogen,
    get_s_blue_water_consumption,
    get_s_green_water_consumption,
    get_s_soil_use_change,
    get_s_biosphere_integrity_genetic_diversity,
    get_s_biosphere_integrity_fonctional_diversity,
    get_s_new_entities,
)

from plot_stripes import get_stripes_collection

from utils import get_warming_stripes_cmap, FIRST, LAST

#%%
# Parameters
N_PLOTS = 9

#%%
#  Data reading
data_dict = {
    "climate_change" : {
        "data" : get_s_climate_change(),
        "y0" : 0,
        "cmap" : get_warming_stripes_cmap()
    },
    "ocean_acidification" : {
        "data" : get_s_ocean_acidification(),
        "y0" : 1,
        "cmap" : get_warming_stripes_cmap()
    },
    "stratosferic_ozone" : {
        "data" : get_s_stratosferic_ozone(),
        "y0" : 2,
        "cmap" : get_warming_stripes_cmap()
    },
    "atmospheric_aerosol" : {
        "data" : get_s_atmospheric_aerosol(),
        "y0" : 3,
        "cmap" : get_warming_stripes_cmap()
    },
    "biogeochimical_phosphore" : {
        "data" : get_s_biogeochimical_phosphore(),
        "y0" : 4,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "biogeochimical_nitrogen" : {
        "data" : get_s_biogeochimical_nitrogen(),
        "y0" : 4.5,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "blue_water_consumption" : {
        "data" : get_s_blue_water_consumption(),
        "y0" : 5,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "green_water_consumption" : {
        "data" : get_s_green_water_consumption(),
        "y0" : 5.5,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "soil_use_change" : {
        "data" : get_s_soil_use_change(),
        "y0" : 6,
        "cmap" : get_warming_stripes_cmap()
    },
    "biosphere_integrity_genetic_diversity" : {
        "data" : get_s_biosphere_integrity_genetic_diversity(),
        "y0" : 7,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "biosphere_integrity_fonctional_diversity" : {
        "data" : get_s_biosphere_integrity_fonctional_diversity(),
        "y0" : 7.5,
        "cmap" : get_warming_stripes_cmap(),
        "height" : 0.5
    },
    "new_entities" : {
        "data" : get_s_new_entities(),
        "y0" : 8,
        "cmap" : get_warming_stripes_cmap()
    }
}

#%%
#  Data stripes creation
for key in data_dict.keys():
    data_dict[key]["col"] = get_stripes_collection(
                        data_dict[key]["data"],
                        cmap = data_dict[key]["cmap"],
                        clim_min = -0.7,
                        clim_max = 0.7,
                        y0 = data_dict[key]["y0"],
                        height = data_dict[key].get("height", 1)
                        )

# %% 
# plots the flag
fig = plt.figure(figsize=(15, 10))

ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()

# create a collection with a rectangle for each year
for key in data_dict.keys():
    ax.add_collection(data_dict[key]["col"])

# Correct the axes and save fig
ax.set_ylim(0, N_PLOTS)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('../img/planetary-flag.png')