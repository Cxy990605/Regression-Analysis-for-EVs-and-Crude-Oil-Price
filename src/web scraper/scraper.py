import requests
import json
import pandas as pd
import csv
import sys
from bs4 import BeautifulSoup as bs
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statistics import mean
from scipy import stats
import yfinance as yf


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

def process_data(data):
    # ev_df = data[0]
    # wti_df = pd.read_csv('wti_spot_price.csv',encoding='utf-8')
    # oxy_df = data[2]
    # wti_df = wti_df.drop('Unnamed: 0',axis=1)
    ev_df = pd.read_csv('car_sales.csv',encoding='utf-8')
    oxy_df = pd.read_csv('OXY_stock.csv',encoding='utf-8')
    wti_df = pd.read_csv('wti_spot_price.csv',encoding='utf-8')
    wti_df = wti_df.drop('Unnamed: 0',axis=1)
    # Combine weekly oxy_close price with wti_price
    oxy_wti = pd.merge(oxy_df, wti_df, on="Date")
    oxy_wti = oxy_wti.rename(columns={"Close": "OXY", "Spot Price": "WTI"})
    oxy_wti.head(5) # oxy_wti = oxy_wti.set_index('Date')



    # Regression line between OXY and WTI
    sns.lmplot(x='OXY', y='WTI', data=oxy_wti, fit_reg=True)


    # #### Even though OXY sounds to be closely related to WTI price, based on the plotted regression line above, it seems there is no significantly relationship.
    # #### Let's check their correlation in a numerical way.


    oxy_wti.corr(method ='pearson')


    # #### correlation coefficent is only 0.188, which implies that there rarely exists relationship between OXY and WTI price


    # Download two new stocks from yfinance, each of which is tightly related to the project
    # CVX: a ticker belonged to GICS sector - Energy - which is the same as OXY
    # ALB: a ticker belonged to GICS sector - Industry - which provides the raw material for electric vehicle

    # How to use these two dataset:
    # 1. Check the correlation among (OXY,WTI,CVX,ALB)
    # 2. Find the top two most interrelated vairables (or called predictors) with either WTI or OXY for EV sales regression analysis


    cvx = yf.download('CVX',start = '2015-01-02',end = '2017-12-30',interval='1d')
    alb = yf.download('ALB',start = '2015-01-02',end = '2017-12-30',interval='1d' )


    # Data preparation
    # Because of the different sources of the data, the first step is to unify their formats, including df.index, the datetime format

    # CVX data
    cvx_df = cvx['Close'].to_frame()
    cvx_df = cvx_df.rename(columns = {'Close':'CVX'})

    index = cvx_df.index
    new_index = []
    for i in index:
        i = i.strftime("%Y-%m-%d")
        new_index.append(i)
    cvx_df = cvx_df.reset_index(drop = True)
    cvx_df.insert(0,"Date",new_index,True)


    # ALB data
    alb_df = alb['Close'].to_frame()
    alb_df = alb_df.rename(columns = {'Close':'ALB'})

    alb_index = alb_df.index
    alb_new_index = []

    for i in alb_index:
        i = i.strftime("%Y-%m-%d")
        alb_new_index.append(i)
    alb_df = alb_df.reset_index(drop = True)
    alb_df.insert(0,"Date",alb_new_index,True)


    data = pd.merge(oxy_wti,cvx_df,on = 'Date')
    data = pd.merge(data,alb_df,on = 'Date')
    data.head(5)


    fig, ax = plt.subplots(figsize=(10,8))


    plt.plot(data['Date'],data['ALB'],label = 'ALB')
    plt.plot(data['Date'],data['OXY'],label = 'OXY')
    plt.plot(data['Date'],data['WTI'],label = 'WTI')
    plt.plot(data['Date'],data['CVX'],label = 'CVX')
    ax.set_xticks(data['Date'][::20])
    ax.set_xticklabels(data['Date'][::20])
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()



    data_scatter = sns.pairplot(data,vars =['OXY','WTI','CVX','ALB'])
    data_scatter.fig.suptitle("scatter plot",fontsize=20,alpha=0.8)
    plt.subplots_adjust(top=0.9)


    data.corr(method ='pearson')


    # ### Correlation analysis
    # Correlation between 0.5 and 0.7 indicate variables moderately correlated.
    # Correlation between 0.3 and 0.5 indicate variables rarely correlated.
    # Based on the correlation report, we are encouraged to choose two pairs:(WTI,CVX)  & (OXY,ALB) for further regression model fitted, NOT inlcuded in this project.
    # In the following analysis, look back on __OXY__ and __WTI__.


    # ## Moving Average Model: MA model
    # Moving averages for more days have a smoother plot, as they’re less reliable on daily fluctuations
    #


    ma_day = [10,20,50]
    ma_oxy = oxy_wti[['Date','OXY']]
    for day in ma_day:
        col = "MA_ %s days" % (str(day))
        ma_oxy[col] = ma_oxy['OXY'].rolling(window = day,center = False).mean()

    ma_oxy.tail()
    # Why check tail?
    # pd.rolling() provides rolling window calculations, and hence before the first rolling window arrives, NA value shows in the oxy_wti.head()


    ma_oxy.plot(figsize = (12,6))



    ma_wti = oxy_wti[['Date','WTI']]
    for day in ma_day:
        col = "MA_ %s days" % (str(day))
        ma_wti[col] = ma_wti['WTI'].rolling(window = day,center = False).mean()

    ma_wti.plot(figsize = (12,6))


    # ### MA analysis
    # __MA__ model plot implies that with the same moving windows, wti price is more stable
    # This result corresponds to the correlation table, showing the relationship between wti and other variables is stronger than that of oxy
    # In this case, let's assume the regression model to predict EV sales will be more fitted, if it includes the predictor wti


    # ## Linear / Multiple Regression Model
    # Extract the 2017 stock data to fit model
    # Choose EV_sales 2017 as Y ; (OXY,WTI,ALB,CVX) as predictors X


    start_index = oxy_wti[oxy_wti['Date']== '2017-01-06'].index
    start_index = 100

    end_index = oxy_wti[oxy_wti['Date']== '2017-12-29'].index
    end_index = 150



    oxy_wti_2017 = oxy_wti.iloc[100:151, :]



    jan = oxy_wti_2017[:4] # dataframe
    feb = oxy_wti_2017[4:8]
    mar = oxy_wti_2017[8:13]
    apr = oxy_wti_2017[13:16]
    may = oxy_wti_2017[16:20]
    jun = oxy_wti_2017[20:25]
    jul = oxy_wti_2017[25:29]
    aug = oxy_wti_2017[29:33]
    sep = oxy_wti_2017[33:38]
    octo = oxy_wti_2017[38:42]
    nov = oxy_wti_2017[42:46]
    dec = oxy_wti_2017[46:51]

    monthly_data = [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]
    oxy_lst = []
    wti_lst = []

    for df in monthly_data:
        oxy_avg = round(mean(df['OXY'].values),2) # for a more concise format to truncate decimal to 2
        wti_avg = round(mean(df['WTI'].values),2)
        oxy_lst.append(oxy_avg)
        wti_lst.append(wti_avg)


    reg_data = {'OXY':oxy_lst,'WTI':wti_lst}
    month_index = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    reg_df = pd.DataFrame(data = reg_data, index = month_index)
    reg_df



    # Web Scrape for 2017 electric cars sales
    html=requests.get('https://insideevs.com/news/344007/monthly-plug-in-ev-sales-scorecard-historical-charts/')
    doc=html.text
    soup = bs(doc, 'html.parser')

    table = soup.find_all('table')
    t_body = soup.find_all('tbody')[1]
    first_table = table[1]

    column_list = []
    for element in first_table.find_all('tr')[0] :
        column_list.append(element.text)

    column_list = list(filter(lambda val: val !=  ' ', column_list))


    NAME_list = []
    JAN_list = []
    FEB_list = []
    MAR_list = []
    APR_list = []
    MAY_list = []
    JUN_list = []
    JULY_list = []
    AUG_list = []
    SEP_list = []
    OCT_list = []
    NOV_list = []
    DEC_list = []
    TOTAL_list = []

    for element in t_body.find_all('tr'):
        NAME_list.append(element.find_all('td')[0].text)
        JAN_list.append(element.find_all('td')[1].text)
        FEB_list.append(element.find_all('td')[2].text)
        MAR_list.append(element.find_all('td')[3].text)
        APR_list.append(element.find_all('td')[4].text)
        MAY_list.append(element.find_all('td')[5].text)
        JUN_list.append(element.find_all('td')[6].text)
        JULY_list.append(element.find_all('td')[7].text)
        AUG_list.append(element.find_all('td')[8].text)
        SEP_list.append(element.find_all('td')[9].text)
        OCT_list.append(element.find_all('td')[10].text)
        NOV_list.append(element.find_all('td')[11].text)
        DEC_list.append(element.find_all('td')[12].text)
        TOTAL_list.append(element.find_all('td')[13].text)

    data = {}
    car_2017 = pd.DataFrame(data)

    body_list = [NAME_list,JAN_list,FEB_list,MAR_list,APR_list,MAY_list,JUN_list,JULY_list,AUG_list,SEP_list,OCT_list,NOV_list,DEC_list,TOTAL_list]

    for i in range(len(column_list)):
        car_2017[column_list[i]] = body_list[i]


    month_sale = car_2017[-3:].iloc[0:1, :]
    month_sale[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]
    month_sale = month_sale.drop(['2017 U.S. EV SALES','TOTAL'],axis=1)
    month_sale = month_sale.T
    month_sale = month_sale.rename(columns = {42:"SALES"})


    # Convert format
    convert_lst = []
    for i in month_sale['SALES']:
        i = int(i.replace(',', ''))
        convert_lst.append(i)

    # Combine data
    sale_data = {'SALES': convert_lst}
    month_index = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    month_sale = pd.DataFrame(data = sale_data, index = month_index)
    reg_df = pd.concat([reg_df, month_sale], axis=1)



    # Variable: OXY
    model_OXY = sm.OLS.from_formula('SALES~OXY',data = reg_df)
    model_OXY.fit()

    OXY = reg_df['OXY']
    SALES = reg_df['SALES']

    # Simple Linear regression formula
    # regr = intercept+ slope * x
    slope = stats.linregress(OXY,SALES)[0]
    intercept = stats.linregress(OXY,SALES)[1]

    regression_OXY = intercept + slope * OXY
    plt.plot(OXY, SALES,'.',OXY,regression_OXY)
    plt.show()



    # Variable: WTI
    model_WTI = sm.OLS.from_formula('SALES~WTI',data = reg_df)
    model_WTI.fit()

    WTI = reg_df['WTI']
    SALES = reg_df['SALES']

    # Simple Linear regression formula
    # regr = intercept+ slope * x
    slope = stats.linregress(WTI,SALES)[0]
    intercept = stats.linregress(WTI,SALES)[1]

    regression_WTI = intercept + slope * WTI
    plt.plot(WTI, SALES,'.',WTI,regression_WTI)
    plt.show()


    # Fit a multiple regression model
    multi_reg=sm.OLS.from_formula('SALES~(OXY + WTI)',data = reg_df)
    multi_reg.fit()
    multi_reg.fit().summary()


    # #### Takeaway:
    # ##### In general, R-squared shows how well the regression model fits the observed data.  In this multiplee regression model, R-squared = 0.151 means that only 15.1% of the data fit the regression model. Hence, it is NOT well-fitted.
    # ##### Meanwhile, the std error is large and p-value is high, both of which implies that it is NOT well-fitted.



    # multi-index dataframe
    # --
    #
    # Create a __multi-index__ dataframe to compare electric vehicles in different years.
    # A more direct way to compare the sales from the same model in different years.


    # Web Scrape for 2018 electric cars sales (in a prettier way, which is better than the one I uploaded as .py--scrape )
    html=requests.get('https://insideevs.com/news/344007/monthly-plug-in-ev-sales-scorecard-historical-charts/')
    doc=html.text
    soup = bs(doc, 'html.parser')

    table = soup.find_all('table')
    t_body = soup.find_all('tbody')[0]
    first_table = table[0]

    column_list = []
    for element in first_table.find_all('tr')[0] :
        column_list.append(element.text)

    column_list = list(filter(lambda val: val !=  ' ', column_list))


    NAME_list = []
    JAN_list = []
    FEB_list = []
    MAR_list = []
    APR_list = []
    MAY_list = []
    JUN_list = []
    JULY_list = []
    AUG_list = []
    SEP_list = []
    OCT_list = []
    NOV_list = []
    DEC_list = []
    TOTAL_list = []

    for element in t_body.find_all('tr'):
        NAME_list.append(element.find_all('td')[0].text)
        JAN_list.append(element.find_all('td')[1].text)
        FEB_list.append(element.find_all('td')[2].text)
        MAR_list.append(element.find_all('td')[3].text)
        APR_list.append(element.find_all('td')[4].text)
        MAY_list.append(element.find_all('td')[5].text)
        JUN_list.append(element.find_all('td')[6].text)
        JULY_list.append(element.find_all('td')[7].text)
        AUG_list.append(element.find_all('td')[8].text)
        SEP_list.append(element.find_all('td')[9].text)
        OCT_list.append(element.find_all('td')[10].text)
        NOV_list.append(element.find_all('td')[11].text)
        DEC_list.append(element.find_all('td')[12].text)
        TOTAL_list.append(element.find_all('td')[13].text)

    data = {}
    car_2018 = pd.DataFrame(data)

    body_list = [NAME_list,JAN_list,FEB_list,MAR_list,APR_list,MAY_list,JUN_list,JULY_list,AUG_list,SEP_list,OCT_list,NOV_list,DEC_list,TOTAL_list]

    for i in range(len(column_list)):
        car_2018[column_list[i]] = body_list[i]



    car_2018 = car_2018[:-3]
    car_2018 = car_2018.iloc[:,:-1] # without the column 'TOTAL'
    car_2018 = car_2018.rename(columns = {"2018 U.S. EV SALES":"BRAND"})
    car_2018.head()



    car_2017 = car_2017[:-3]
    car_2017 = car_2017.iloc[:,:-1] # without the column 'TOTAL'
    car_2017 = car_2017.rename(columns = {"2017 U.S. EV SALES":"BRAND"})
    car_2017.head()


    brands = pd.merge(car_2017,car_2018, on='BRAND')['BRAND']
    brand_name = []
    for i in brands.tolist():
        i=i.rstrip('\xa0')
        brand_name.append(i)
    # len(brand_name) 15
    # print(brand_name)
    # ['Tesla Model S*', 'Tesla Model X*', 'Toyota Prius Prime', 'Nissan LEAF', 'Ford Fusion Energi', 'Ford C-Max Energi', 'BMW i3 (BEV + REx)', 'Fiat 500e**', 'Chrysler Pacifica Hybrid**', 'Volkswagen e-Golf', 'Ford Focus Electric', 'Mercedes B250e', 'smart ED', 'BMW i8', 'Mitsubishi Outlander PHEV']



    columns = list(car_2017.columns)[1:] # ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    years = ["2017","2018"]
    index = []

    # pair brands with different years,format as :('Tesla Model S*', '2017'),('Tesla Model S*', '2018'),
    for brand in brand_name:
        for i in years:
            tmp = []
            tmp.append(brand)
            tmp.append(i)
            index.append(tmp)


    # Convert list_item to tuples
    tuples_lst = []
    for item in index:
        item = tuple(item)
        tuples_lst.append(item)

    index_level = pd.MultiIndex.from_tuples(tuples_lst,names = ['brand','year'])



    df = pd.concat([car_2017,car_2018])
    result_tmp = []
    for i in brands.tolist():
        tmp = df.loc[df["BRAND"] == i]
        res = tmp.values.tolist()
        result_tmp.append(res)

    result_final = []
    for j in result_tmp:
        result_final.append(j[0])
        result_final.append(j[1])


    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    octo = []
    nov = []
    dec = []

    for i in result_final:
        jan.append(i[1])
        feb.append(i[2])
        mar.append(i[3])
        apr.append(i[4])
        may.append(i[5])
        jun.append(i[6])
        jul.append(i[7])
        aug.append(i[8])
        sep.append(i[9])
        octo.append(i[10])
        nov.append(i[11])
        dec.append(i[12])



    data={'JAN':jan,
          'FEB':feb,
          'MAR':mar,
          'APR':apr,
          'MAY':may,
          'JUN':jun,
          'JUL':jul,
          'AUG':aug,
          'SEP':sep,
          'OCT':octo,
          'NOV':nov,
          'DEC':dec}
    car_df = pd.DataFrame(data,index = index_level)
    car_df.head(10)




    # ## Appendix
    # #### Further exploration of web_scrape



    # Collect WTI monthly for EV mmonthly sales:
    api_key ='vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc'
    url = 'https://api.eia.gov/series/?api_key=' + api_key +'&series_id='+'PET.RWTC.M'
    r=requests.get(url)
    data=r.json()
    oil_price=data['series'][0]['data']


    result = []
    date_lst = []
    price_lst = []

    for i in oil_price:
        if '201612'<i[0]<'201901':
            result.append(i)
    result.sort(key=lambda x: x[0])

    for i in result:
        date=datetime.strptime(i[0], '%Y%m')
        date=date.strftime('%Y-%m')
        date_lst.append(date)

    for i in result:
        price = i[1]
        price_lst.append(price)

    d={'Date':date_lst,
          'WTI': price_lst}
    result_df = pd.DataFrame(data=d)

    result_df.head(5)



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


    process_data(data)


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
