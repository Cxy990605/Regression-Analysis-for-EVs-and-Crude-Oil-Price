import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
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
            car_df = pd.read_csv(path)
            print(f"Read data from {path}")
        except:
            sys.exit(f"Could not read {path}")
    else:
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
        car_df = pd.DataFrame(data=d)

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


        car_df= pd.DataFrame(data,brands)
        path = 'car_sales.csv'
        car_df.to_csv(path)
        print(f"Wrote data to {path}")

    with pd.option_context('display.max_rows', 6 if sample_p else None,
                           'display.max_columns', None,
                           'display.precision', 3):
        print(car_df)

if __name__ == '__main__':
    main()
