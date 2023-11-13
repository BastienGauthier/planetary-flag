
#%% Importation
import pandas as pd
import numpy as np

from utils import FIRST, LAST

#%% Data reading
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

def get_all_data_dict(filename = '../data/planetary_boundaries_data.xlsx'):
    return pd.read_excel(filename,sheet_name=None)

#%% Data creation
def get_random_data():

    return pd.Series(
        data= np.random.uniform(-1, 1, LAST - FIRST + 1),
        index= range(FIRST, LAST + 1)
    )


#%% Data formatting

def get_data(data_all,df_synthesis,idx):

    df = data_all[df_synthesis.loc[idx,"sheetname"]]

    df = df[df_synthesis.loc[idx,["date_label","value_label"]]]

    df.columns = ["year","value"]

    return df.set_index("year")


def uniformize_date(df, year_index= range(FIRST, LAST + 1)):

    df_extract = df.reindex(
        set(list(df.index) + list(year_index))
        ).sort_index().interpolate()

    return df_extract.loc[year_index,:].squeeze()


def get_s_climate_change(data_all,df_synthesis,idx=1.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_ocean_acidification(data_all,df_synthesis,idx=2.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_stratosferic_ozone(data_all,df_synthesis,idx=3.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_atmospheric_aerosol(data_all,df_synthesis,idx=4.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_biogeochimical_phosphore(data_all,df_synthesis,idx=5.1):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_biogeochimical_nitrogen(data_all,df_synthesis,idx=5.2):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_blue_water_consumption(data_all,df_synthesis,idx=6.1):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_green_water_consumption(data_all,df_synthesis,idx=6.2):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_land_use_change(data_all,df_synthesis,idx=7.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_biosphere_integrity_genetic_diversity(data_all,df_synthesis,idx=8.1):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_biosphere_integrity_fonctional_diversity(data_all,df_synthesis,idx=8.2):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)


def get_s_new_entities(data_all,df_synthesis,idx=9.0):
    df = get_data(data_all,df_synthesis,idx)
    return uniformize_date(df)