import urllib
from bs4 import BeautifulSoup
import pandas as pd


def get_url(path_to_url):
    return urllib.request.urlopen(path_to_url)


class CountryCodes:

    def __init__(self):
        self.output_countries_from_url = self.output_countries_from_url()
        self.filter_beautiful_soup = self.filter_beautiful_soup()

    def output_countries_from_url(self):
        country_code_soup = BeautifulSoup(get_url("https://www.iban.com/country-codes"), "html.parser")
        country_code_table = country_code_soup.find('table')
        table_country_code_rows = country_code_table.find_all('tr')
        countries_data = []
        for tr in table_country_code_rows:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            if row:
                countries_data.append(row)
        return pd.DataFrame(countries_data, columns=["Area", "Alpha-2 code", "Alpha-3 code", "numeric"])

    def filter_beautiful_soup(self):
        df_filtered_country_codes = self.output_countries_from_url.drop(['Alpha-2 code'], axis=1)
        df_filter = df_filtered_country_codes.rename(columns={"Alpha-3 code": "Alpha-3"})
        df_filter['Area'] = df_filter['Area'].str.replace(" " r"\(.*\)", "", regex=True)

        return df_filter
