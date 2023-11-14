# Importation
from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib
from utils import FIRST, LAST, N_PLOTS

# Parameters
matplotlib.rcParams.update({'font.size': 22})


def plot_planetary_flag(data_dict, axes):

    new_data_dict = deepcopy(data_dict)

    fig = plt.figure(figsize=(15, 10))

    ax = fig.add_axes([0, 0, 1, 1])
    if not(axes): 
        ax.set_axis_off()
    else:
        labels = [str.capitalize(key.replace('_',' ')) for key in new_data_dict.keys()]
        ticks = [new_data_dict[key]["y0"] + data_dict[key].get("height", 1)/2 
                    for key in new_data_dict.keys()]
        ax.set_yticks(ticks, labels)

    # create a collection with a rectangle for each year
    for key in new_data_dict.keys():
        ax.add_collection(new_data_dict[key]["col"])

    # Correct the axes and save fig
    ax.set_ylim(0, N_PLOTS)
    ax.set_xlim(FIRST, LAST + 1)

    return fig, ax

def plot_graphic_planetary_flag(data_dict):

    fig, ax = plot_planetary_flag(
        data_dict, 
        axes = False
        )
    
    fig.savefig('../img/planetary-flag.png')

    return fig

def plot_detailled_planetary_flag(data_dict):

    fig, ax = plot_planetary_flag(
        data_dict, 
        axes = True
        )
    
    ax.set_title("Planetary boundaries")
    
    fig.savefig('../img/detailled-planetary-flag.png')

    return fig