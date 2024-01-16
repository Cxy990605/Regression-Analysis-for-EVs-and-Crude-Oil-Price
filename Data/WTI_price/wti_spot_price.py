import pandas as pd
import sys
import requests
import numpy as np
from datetime import datetime


def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: sample_scraper.py [-h] [--scrape] [--static <PATH_TO_DATASET>]")
        print("   with option --scrape, program will display only up to 6 entries")
        sys.exit(0)
    sample_p = ('--scrape' in sys.argv)  # Output only a sample of 6 entries
    try:
       static_kw_pos = sys.argv.index('--static')  # position of '--static' keyword in argv list
       path = sys.argv[static_kw_pos+1]            # dataset filename (input)
    except:
       path = None

    if path:
        try:
            result_df = pd.read_csv(path)
            print(f"Read data from {path}")
        except:
            sys.exit(f"Could not read {path}")
    else:

        api_key ='vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc'

        url = 'https://api.eia.gov/series/?api_key=' + api_key +'&series_id='+'PET.RWTC.W'
        #https://api.eia.gov/series/?api_key=vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc&series_id=PET.RWTC.W
        #headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
        r=requests.get(url)
        #print(r)
        data=r.json()
        startDate = '2015-01-01'
        endDate = '2019-01-01'
        oil_price=data['series'][0]['data']


        result = []
        date_lst = []
        price_lst = []

        for i in oil_price:
            if '20150101'<i[0]<'20190101':
                result.append(i)
        result.sort(key=lambda x: x[0])

        for i in result:
            date=datetime.strptime(i[0], '%Y%m%d')
            date=date.strftime('%Y-%m-%d')
            date_lst.append(date)
        #print(date_lst)

        for i in result:
            price = i[1]
            price_lst.append(price)
        #print(price_lst)

        d={'Date':date_lst,
              'Spot Price': price_lst}
        result_df=pd.DataFrame(data=d)
        result_df.head(5)

        path = 'wti_spot_price.csv'
        result_df.to_csv(path)
        print(f"Wrote data to {path}")

    with pd.option_context('display.max_rows', 6 if sample_p else None,
                           'display.max_columns', None,
                           'display.precision', 3):
        print(result_df)


    '''
    key='vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc'
    time_slot=['PET.RWTC.D','PET.RWTC.W','PET.RWTC.M']
    start_day = '2015-01-01'
    end_day = '2019-01-01'
    '''
if __name__ == '__main__':
    main()
