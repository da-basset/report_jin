import sys
from pathlib import Path

# Add project root to sys.path so the "app" package can be imported
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Import "app" package
from ..tools.fred_requests import WebRequest

class NASDAQ_Data():
    
    def get_data():
        observation_start_date = "2020-01-01"
        observation_end_date = "9999-12-31"
        realtime_start_date = "2026-06-16"
        realtime_end_date = "2026-06-16"
        set_frequency = "a"

        data = WebRequest.get_fred_nasdaq_series_data(observation_start=observation_start_date, observation_end=observation_end_date, realtime_start=realtime_start_date, realtime_end=realtime_end_date, frequency=set_frequency)
        #start_of_year_data = float(data['observations'][0]['value'])
        return data