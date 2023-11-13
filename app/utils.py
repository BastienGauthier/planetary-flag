from matplotlib.colors import ListedColormap

## Scale
FIRST = 1850
LAST = 2021  # inclusive

## Reference period for the center of the color scale
FIRST_REFERENCE = 1971
LAST_REFERENCE = 2000

def get_warming_stripes_cmap():
    # the colors in this colormap come from http://colorbrewer2.org
    # the 8 more saturated colors from the 9 blues / 9 reds
    return ListedColormap([
    '#08306b', '#08519c', '#2171b5', '#4292c6',
    '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
    '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
    '#ef3b2c', '#cb181d', '#a50f15', '#67000d',
    ])

def get_planetary_flag_cmap():
    return ListedColormap([
        '#005a32','#238b45','#41ab5d','#74c476',
        '#a1d99b','#c7e9c0','#e5f5e0','#f7fcf5',
        '#fff5eb','#fee6ce','#fdd0a2','#fdae6b',
        '#fd8d3c','#f16913','#d94801','#8c2d04'
          ])

