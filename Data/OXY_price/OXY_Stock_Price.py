import requests
import json
import pandas as pd
import csv
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import sys

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
            data_df = pd.read_csv(path)
            print(f"Read data from {path}")
        except:
            sys.exit(f"Could not read {path}")
    else:
        key='wCgHNXA4XE-naxGvQt6X'
        url='https://data.nasdaq.com/api/v3/datasets/WIKI/OXY/data.json?start_date=2015-01-01&end_date=2018-03-27&order=asc&column_index=4&api_key='+key
        r=requests.get(url)
        json_data=r.json()

        cols=json_data['dataset_data']['column_names'] #['Date', 'Close']
        data=json_data['dataset_data']['data']
        data_df=pd.DataFrame(data,columns=cols)
        #data_df.head(5)

        path = 'OXY_stock.csv'

        data_df.to_csv(path,index=False)

        print(f"Wrote data to {path}")



    with pd.option_context('display.max_rows', 6 if sample_p else None,
                           'display.max_columns', None,
                           'display.precision', 3):
        print(data_df)

if __name__ == '__main__':
    main()




# # plot
# x = data_df['Date']
# x = x.to_numpy()
# y = data_df['Close']
# plt.figure(figsize=(8,8))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
# plt.title("OXY_STOCK_PRICE 2015-2018")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.plot(x, y)
# plt.gcf().autofmt_xdate()
# plt.show()


# def stock_price(key,start_day,end_day):
#     url='https://data.nasdaq.com/api/v3/datasets/WIKI/OXY/data.json?start_date='+start_day+'&end_date='+end_day+'&order=asc&column_index=4&api_key='+key
#     r=requests.get(url)
#     json_data=r.json()
#
#     cols=json_data['dataset_data']['column_names']
#     data=json_data['dataset_data']['data']
#     data.insert(0,cols)
#
#     with open("stock_price .csv", "a", newline = '', encoding = 'utf-8') as fhand:
#         writer = csv.writer(fhand ,delimiter = ',')
#         writer.writerows(data)
