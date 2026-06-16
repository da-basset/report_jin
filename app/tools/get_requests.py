import requests
import json
import datetime
import os

# Begin Global Variables
api_token = os.environ.get('FRED_API_TOKEN')
#date = datetime.UTC
# End Global Variables

class WebRequest():
    
    def get_fred_CPI_series_data(observation_start, frequency, series_id="FPCPITOTLZGUSA", format = json):
        '''
        Fetch FRED series observations from observation_start to the series end.

        Parameters
        - observation_start (str|None): Start date "YYYY-MM-DD". If None or omitted, returns from the earliest available date.
        - frequency (str|None): Output frequency (short or long form). Common values:
            d / daily
            w / weekly
            bw / biweekly
            m / monthly
            q / quarterly
            sa / semiannual
            a / annual
          If None or omitted, uses the series' native frequency.
        - series_id (str): FRED series id (default "FPCPITOTLZGUSA").
        - format: Response format (default: JSON).

        Returns
        - str: Raw API response text.

        See: https://fred.stlouisfed.org/docs/api/fred/series_observations.html
        '''
        request = requests.get(f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_token}&file_type=json&observation_start={observation_start}&frequency={frequency}')
        output = request.json()
        return output
    
    def get_fred_SP500_series_data(observation_start, observation_end, realtime_start, realtime_end, frequency, series_id="SP500", format = json):
        request = requests.get(f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_token}&file_type=json&observation_start={observation_start}&observation_end={observation_end}&realtime_start={realtime_start}&realtime_end={realtime_end}&frequency={frequency}')
        output = request.json()
        return output
    
