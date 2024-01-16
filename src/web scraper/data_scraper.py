import requests
import json
import pandas as pd
import csv
import sys
from bs4 import BeautifulSoup as bs
from datetime import datetime


def read_from_local():
    ev_df = pd.read_csv('car_sales.csv',encoding='utf-8')
    oxy_df = pd.read_csv('OXY_stock.csv',encoding='utf-8')
    wti_df = pd.read_csv('wti_spot_price.csv',encoding='utf-8')
    return [ev_df,oxy_df,wti_df]

def scrape_from_web():

    #ev_car_df

    html=requests.get('https://insideevs.com/news/344007/monthly-plug-in-ev-sales-scorecard-historical-charts/')
    doc=html.text
    soup = bs(doc, 'html.parser')
    #print(soup.prettify())
    soup=soup.find_all('td')
    brands=[]
    for i in range(0,600,14):
        brand=soup[i].find('a').text
        brands.append(brand)# len(brands): 43
                            # brands
    #print(brands)

    jan_sale=[]
    for i in range(1,600,14):
        sale=soup[i].get_text()
        jan_sale.append(sale)
        #len(jan_sale):43
    jan_sale=list(map(lambda x:x.replace('\xa0','0'),jan_sale))
    #print(jan_sale)


    feb_sale=[]
    for i in range(2,600,14):
        sale=soup[i].get_text()
        feb_sale.append(sale)
    feb_sale=list(map(lambda x:x.replace('\xa0','0'),feb_sale))
    #print(feb_sale)


    mar_sale=[]
    for i in range(3,600,14):
        sale=soup[i].get_text()
        mar_sale.append(sale)
    mar_sale=list(map(lambda x:x.replace('\xa0','0'),mar_sale))
    #print(mar_sale)


    apr_sale=[]
    for i in range(4,600,14):
        sale=soup[i].get_text()
        apr_sale.append(sale)
    apr_sale=list(map(lambda x:x.replace('\xa0','0'),apr_sale))
    #print(apr_sale)


    may_sale=[]
    for i in range(5,600,14):
        sale=soup[i].get_text()
        may_sale.append(sale)
    may_sale=list(map(lambda x:x.replace('\xa0','0'),may_sale))
    #print(may_sale)



    jun_sale=[]
    for i in range(6,600,14):
        sale=soup[i].get_text()
        jun_sale.append(sale)
    jun_sale=list(map(lambda x:x.replace('\xa0','0'),jun_sale))
    #print(jun_sale)


    jul_sale=[]
    for i in range(7,600,14):
        sale=soup[i].get_text()
        jul_sale.append(sale)
    jul_sale=list(map(lambda x:x.replace('\xa0','0'),jul_sale))
    #print(jul_sale)


    aug_sale=[]
    for i in range(8,600,14):
        sale=soup[i].get_text()
        aug_sale.append(sale)
    aug_sale=list(map(lambda x:x.replace('\xa0','0'),aug_sale))
    #print(aug_sale)


    sep_sale=[]
    for i in range(9,600,14):
        sale=soup[i].get_text()
        sep_sale.append(sale)
    sep_sale=list(map(lambda x:x.replace('\xa0','0'),sep_sale))
    #print(sep_sale)



    oct_sale=[]
    for i in range(10,600,14):
        sale=soup[i].get_text()
        oct_sale.append(sale)
    oct_sale=list(map(lambda x:x.replace('\xa0','0'),oct_sale))
    #print(oct_sale)


    nov_sale=[]
    for i in range(11,600,14):
        sale=soup[i].get_text()
        nov_sale.append(sale)
    nov_sale=list(map(lambda x:x.replace('\xa0','0'),nov_sale))
    #print(nov_sale)



    dec_sale=[]
    for i in range(12,605,14):
        sale=soup[i].get_text()
        dec_sale.append(sale)
    dec_sale=list(map(lambda x:x.replace('\xa0','0'),dec_sale))
    #print(dec_sale)



    d = {'col1': [1, 2], 'col2': [3, 4]}
    ev_df = pd.DataFrame(data=d)

    data={'Jan':jan_sale,
          'Fed':feb_sale,
          'March':mar_sale,
          'April':apr_sale,
          'May':may_sale,
          'June':jun_sale,
          'July':jul_sale,
          'Aug':aug_sale,
          'Sep':sep_sale,
          'Oct':oct_sale,
          'Nov':nov_sale,
          'Dec':dec_sale}


    ev_df= pd.DataFrame(data,brands)
    path = 'car_sales.csv'
    ev_df.to_csv(path)

    print(f"Wrote car sales data to {path}")




    #wti_spot_price
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
    wti_df=pd.DataFrame(data=d)
    wti_df.head(5)

    path = 'wti_spot_price.csv'
    wti_df.to_csv(path)
    print(f"Wrote WTI spot price data to {path}")




    #OXY_STOCK_PRICE
    key='wCgHNXA4XE-naxGvQt6X'
    url='https://data.nasdaq.com/api/v3/datasets/WIKI/OXY/data.json?start_date=2015-01-01&end_date=2018-03-27&order=asc&column_index=4&api_key='+key
    r=requests.get(url)
    json_data=r.json()

    cols=json_data['dataset_data']['column_names'] #['Date', 'Close']
    data=json_data['dataset_data']['data']
    oxy_df=pd.DataFrame(data,columns=cols)
    #data_df.head(5)

    path = 'OXY_stock.csv'

    oxy_df.to_csv(path,index=False)

    print(f"Wrote OXY price data to {path}")

    return [ev_df,wti_df,oxy_df]


def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: sample_scraper.py [-h] [--static]")
        sys.exit(0)
    sample_p = ('--static' in sys.argv)  # Output only a sample of 6 entries
    if sample_p:
        print("read data from local file")
        data = read_from_local()
    else:
        print('please wait for several minutes to grab the data')
        data = scrape_from_web()

    for i in data:
        with pd.option_context('display.max_rows', 6,
                               'display.max_columns', None,
                               'display.precision', 3):
            print(i)
    print("succeed!")
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
