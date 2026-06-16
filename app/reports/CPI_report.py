import datetime
import math
import sys
from pathlib import Path

# Add project root to sys.path so the "app" package can be imported
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Import "app" package
from ..tools.fred_requests import WebRequest

### Begin Global Variables ###
date = datetime.UTC

# WebRequest Variables #
start_date = "2020-01-01"
set_frequency = "a"
### End Global Variables ###

class CPI_data():
    date_start = start_date
    def clean_cpi_data(cpi_data):
        value_list = []
        observations = cpi_data['observations']

        for i, value in enumerate(observations):
            value_list.append(observations[i]['value'])
        
        return value_list
    
    def compound_CPI_values(value_list):
        compound_list = []

        for value in value_list:
            compound_data = (1 + float(value)/100)
            compound_list.append(compound_data)

        return compound_list
    
    def generate_CPI_percentage(compound_list):
        final_factor = math.prod(compound_list)
        CPI_fractor = final_factor - 1
        CPI_percentage = CPI_fractor * 100
        return CPI_percentage
    
    def main_report():
        data = WebRequest.get_fred_CPI_series_data(observation_start=start_date, frequency=set_frequency)
        clean_data = CPI_data.clean_cpi_data(data)
        compound_data = CPI_data.compound_CPI_values(clean_data)
        final_percentage = CPI_data.generate_CPI_percentage(compound_data)
        return final_percentage









