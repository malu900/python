import pandas as pd
import os
from data.CountryCodes import CountryCodes
import numpy as np
from datetime import datetime

from data.CreateNewCsv import CreateNewCsv


class CovidMap:

    def get_map_data(self):
        covid_map = pd.DataFrame(CreateNewCsv().get_covid_csv())
        # covid_map["Date"] = CreateNewCsv().get_covid_csv["Date"].replace(',', '', regex=True)
        # date = 'Dec 31 2019'
        # covid_map["Date"] = pd.to_datetime(covid_map["Date"], format='%b %d % Y')
        # print(covid_map)
        # newdate = datetime.strptime(date, '%b %d %Y').date()
        return covid_map
