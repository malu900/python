import pandas as pd
import os
from data.CountryCodes import CountryCodes
import numpy as np


def get_csv(path_to_csv):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), path_to_csv))


class CreateNewCsv:

    def __init__(self):
        self.merge_csv_with_country_codes = self.merge_csv_with_country_codes()
        self.get_covid_csv = self.get_covid_csv()

    def merge_csv_with_country_codes(self):
        df_merged_country_codes_livestock = CountryCodes().filter_beautiful_soup.merge(
            get_csv("../datasets/FAOSTAT_livestock_patterns.csv"), on="Area", how='inner')
        df_country_codes_livestock = df_merged_country_codes_livestock.drop(['Year Code', 'Domain'], axis=1)
        df_country_codes_livestock['Area'] = df_country_codes_livestock['Area'].str.replace(" " r"\(.*\)", "",
                                                                                            regex=True)
        return df_country_codes_livestock

    def get_covid_csv(self):
        df_merged_country_codes_livestock = CountryCodes().filter_beautiful_soup.merge(
            get_csv("../datasets/total-covid-deaths-per-million.csv"), on="Area", how='inner')
        df_country_codes_livestock = df_merged_country_codes_livestock.rename(columns={'Total confirmed deaths due to COVID-19 per million people (deaths per million)': 'deaths'})

        df_country_codes_livestock['Area'] = df_country_codes_livestock['Area'].str.replace(" " r"\(.*\)", "",
                                                                                            regex=True)
        return df_country_codes_livestock
