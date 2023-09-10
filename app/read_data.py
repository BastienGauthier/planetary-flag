
import pandas as pd
import numpy as np

from utils import FIRST, LAST

def get_df_temperature_anomaly():
    # data from
    # https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/time_series/HadCRUT.4.6.0.0.annual_ns_avg.txt

    df = pd.read_fwf(
        '../data/HadCRUT.4.6.0.0.annual_ns_avg.txt',
        index_col=0,
        usecols=(0, 1),
        names=['year', 'anomaly'],
        header=None,
    )

    return df.loc[FIRST:LAST, 'anomaly'].dropna()

def get_random_data():

    return pd.Series(
        data= np.random.uniform(-1, 1, LAST - FIRST + 1),
        index= range(FIRST, LAST + 1)
    )

def get_s_climate_change():
    return get_random_data()

def get_s_ocean_acidification():
    return get_random_data()

def get_s_stratosferic_ozone():
    return get_random_data()

def get_s_atmospheric_aerosol():
    return get_random_data()

def get_s_biogeochimical_phosphore():
    return get_random_data()

def get_s_biogeochimical_nitrogen():
    return get_random_data()

def get_s_blue_water_consumption():
    return get_random_data()

def get_s_green_water_consumption():
    return get_random_data()

def get_s_soil_use_change():
    return get_random_data()

def get_s_biosphere_integrity_genetic_diversity():
    return get_random_data()

def get_s_biosphere_integrity_fonctional_diversity():
    return get_random_data()

def get_s_new_entities():
    return get_random_data()