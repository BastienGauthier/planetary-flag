# %%
# Importation
import matplotlib.pyplot as plt
import pandas as pd

from read_data import (
    get_all_data_dict,
    get_s_climate_change,
    get_s_ocean_acidification,
    get_s_stratosferic_ozone,
    get_s_atmospheric_aerosol,
    get_s_biogeochimical_phosphore,
    get_s_biogeochimical_nitrogen,
    get_s_blue_water_consumption,
    get_s_green_water_consumption,
    get_s_land_use_change,
    get_s_biosphere_integrity_genetic_diversity,
    get_s_biosphere_integrity_fonctional_diversity,
    get_s_new_entities,
)

from plot_stripes import get_stripes_collection

from utils import get_planetary_flag_cmap, FIRST, LAST

#%%
# Parameters
N_PLOTS = 9
general_cmap = get_planetary_flag_cmap()

#%%
#  Data reading
data_all = get_all_data_dict()
df_synthesis = data_all["synthese"].set_index('id')

#  Data formatting
data_dict = {
    "climate_change" : {
        "idx" : 1.0,
        "data" : get_s_climate_change(data_all,df_synthesis),
        "y0" : 0,
        "cmap" : general_cmap
    },
    "ocean_acidification" : {
        "idx" : 2.0,
        "data" : get_s_ocean_acidification(data_all,df_synthesis),
        "y0" : 1,
        "cmap" : general_cmap
    },
    "stratosferic_ozone" : {
        "idx" : 3.0,
        "data" : get_s_stratosferic_ozone(data_all,df_synthesis),
        "y0" : 2,
        "cmap" : general_cmap
    },
    "atmospheric_aerosol" : {
        "idx" : 4.0,
        "data" : get_s_atmospheric_aerosol(data_all,df_synthesis),
        "y0" : 3,
        "cmap" : general_cmap
    },
    "biogeochimical_phosphore" : {
        "idx" : 5.1,
        "data" : get_s_biogeochimical_phosphore(data_all,df_synthesis),
        "y0" : 4,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "biogeochimical_nitrogen" : {
        "idx" : 5.2,
        "data" : get_s_biogeochimical_nitrogen(data_all,df_synthesis),
        "y0" : 4.5,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "blue_water_consumption" : {
        "idx" : 6.1,
        "data" : get_s_blue_water_consumption(data_all,df_synthesis),
        "y0" : 5,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "green_water_consumption" : {
        "idx" : 6.2,
        "data" : get_s_green_water_consumption(data_all,df_synthesis),
        "y0" : 5.5,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "land_use_change" : {
        "idx" : 7.0,
        "data" : get_s_land_use_change(data_all,df_synthesis),
        "y0" : 6,
        "cmap" : general_cmap
    },
    "biosphere_integrity_genetic_diversity" : {
        "idx" : 8.1,
        "data" : get_s_biosphere_integrity_genetic_diversity(data_all,df_synthesis),
        "y0" : 7,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "biosphere_integrity_fonctional_diversity" : {
        "idx" : 8.2,
        "data" : get_s_biosphere_integrity_fonctional_diversity(data_all,df_synthesis),
        "y0" : 7.5,
        "cmap" : general_cmap,
        "height" : 0.5
    },
    "new_entities" : {
        "idx" : 9.0,
        "data" : get_s_new_entities(data_all,df_synthesis),
        "y0" : 8,
        "cmap" : general_cmap
    }
}

#%% 
# Save processed result
df_processed = pd.concat([
        item["data"].rename(key) 
            for key,item in data_dict.items()
     ],axis=1)

df_processed.to_csv('../data/processed/planetary_boundaries_processed.csv')

#%% 
# Deal with cmap & signs
for key in data_dict.keys():
    s_key = df_synthesis.loc[data_dict[key]["idx"],:]
    if s_key.sign == "negative": # inverse all
        data_dict[key]["data"] *= -1
        data_dict[key]["clim_min"] = -s_key.color_limit_max
        data_dict[key]["clim_max"] = -s_key.color_limit_min
    else:
        data_dict[key]["clim_min"] = s_key.color_limit_min
        data_dict[key]["clim_max"] = s_key.color_limit_max        

#%%
#  Data stripes creation
for key in data_dict.keys():
    data_dict[key]["col"] = get_stripes_collection(
                        data_dict[key]["data"],
                        cmap = data_dict[key]["cmap"],
                        clim_min = data_dict[key]["clim_min"] ,
                        clim_max = data_dict[key]["clim_max"] ,
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