import datetime
import math
import sys
from pathlib import Path

# Add project root to sys.path so the "app" package can be imported
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Import "app" package
from app.tools.get_requests import WebRequest

# Begin Global Variables
date = datetime.UTC
# End Global Variables

class SP500():

    def get_start_of_year_value():
        observation_start_date = "2026-01-01"
        observation_end_date = "9999-12-31"
        realtime_start_date = "2026-06-16"
        realtime_end_date = "2026-06-16"
        set_frequency = "m"

        data = WebRequest.get_fred_SP500_series_data(observation_start=observation_start_date, observation_end=observation_end_date, realtime_start=realtime_start_date, realtime_end=realtime_end_date, frequency=set_frequency)
        start_of_year_data = float(data['observations'][0]['value'])
        return start_of_year_data
    
    def get_today_value():
        observation_start_date = "2026-06-15"
        observation_end_date = "9999-12-31"
        realtime_start_date = "2026-06-16"
        realtime_end_date = "2026-06-16"
        set_frequency = "d"

        data = WebRequest.get_fred_SP500_series_data(observation_start=observation_start_date, observation_end=observation_end_date, realtime_start=realtime_start_date, realtime_end=realtime_end_date, frequency=set_frequency)
        todays_data = float(data['observations'][0]['value'])
        return todays_data

    
    def clean_SP500_data(sp500_data):
        return sp500_data
    
    def main_report():
        start_of_year = SP500.get_start_of_year_value()
        today_value = SP500.get_today_value()
        difference = today_value - start_of_year
        return difference

'''
x = SP500.main_report()
print(x)
'''