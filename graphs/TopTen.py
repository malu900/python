from data.CreateNewCsv import CreateNewCsv
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class TopTen:

    def __init__(self):
        self.get_by_year = self.get_by_year()

    def get_by_year(self):
        df_2003_agriculture = CreateNewCsv().merge_csv_with_country_codes[
            CreateNewCsv().merge_csv_with_country_codes['Year'] == 2016].copy()
        return df_2003_agriculture

    # def get_unique(self):
    #     return self.get_by_year.drop_duplicates()

    def df_get_top_eleven(self):
        top_ten = self.get_by_year.nlargest(12, ['Value']).sort_values('Value', ascending=True).copy()
        return top_ten

    def top_eleven_bool(self):
        bool_top = (self.df_get_top_eleven()['Value'] != self.df_get_top_eleven()['Value'].max()) & \
                   (self.df_get_top_eleven()['Value'] != self.df_get_top_eleven()['Value'].min())
        return bool_top

    def top_ten_bool(self):
        bool_top = self.df_get_top_eleven()['Value'] != self.df_get_top_eleven().nlargest(10, 'Value')
        return bool_top

    def top_without_both(self):
        bool_top = self.df_get_top_eleven()['Value'] != self.df_get_top_eleven().nsmallest(10, 'Value')
        return bool_top

    def min_top_ten(self):
        min_eleven = self.get_by_year.nsmallest(10, ['Value'])
        return min_eleven
