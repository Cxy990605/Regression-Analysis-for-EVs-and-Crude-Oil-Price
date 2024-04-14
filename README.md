* **Introduction**
##### With the evolution of ESG, the rise of Electric Vehicles (EVs) bring about opportunities and challenges for power industry. 
##### It is an intuitve that as the gosiline price goes higher, people are more willing to buy EVs which are fueled by electricity instead of gasoline.
##### This project focuses on the relationship between sales of Evs and crude oil price.

---
* **Data Visualization**
  > Moving Average Model for the crude oil price
<img width="714" alt="Screen Shot 2024-04-14 at 12 51 30 AM" src="https://github.com/Cxy990605/Regression-Analysis-for-EVs-and-Crude-Oil-Price/assets/99168940/edda93ac-61c3-4504-b312-a62c930b50d8">

  > Regression Model for OXY and WTI crude oil price
  <img width="495" alt="Screen Shot 2024-04-14 at 12 51 20 AM" src="https://github.com/Cxy990605/Regression-Analysis-for-EVs-and-Crude-Oil-Price/assets/99168940/87530efb-4bad-43f2-a5fb-e27aced69bc8">

  > Regression Model for EVs sales and crude oil price
  <img width="644" alt="Screen Shot 2024-04-14 at 12 59 39 AM" src="https://github.com/Cxy990605/Regression-Analysis-for-EVs-and-Crude-Oil-Price/assets/99168940/97f8f1de-8c5e-4173-82cf-94dbf5e1d47c">

  
  > Multi-index Table for EVs
  <img width="716" alt="Screen Shot 2024-04-14 at 12 58 30 AM" src="https://github.com/Cxy990605/Regression-Analysis-for-EVs-and-Crude-Oil-Price/assets/99168940/c3c45765-fcdb-4631-9298-3417b1f7c308">


---
Data Sources:

* **OXY_stock.csv** (from NASDAQ)[^1]  
api_key ='wCgHNXA4XE-naxGvQt6X'  
* **wti_spot_price.csv** (from EIA)[^2]  
api_key ='vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc'
* car_sales.csv[^3]


---
Notes:
1. WTI crude oil price is an international crude oil transaction benchmark.
2. OXY, Occidental Petroleum Corporation, is a company engaged in hydrocarbon exploration and petrochemical manufacturing.


[^1]: <https://data.nasdaq.com/api/v3/datasets/WIKI/OXY/data.json?start_date=2015-01-01&end_date=2018-03-27&order=asc&column_index=4&api_key=wCgHNXA4XE-naxGvQt6X>
[^2]: <https://api.eia.gov/series/?api_key=vT2MbTCiEVzdJdsxQe1VVKxVBsmwrgbJroVhrDxc&series_id=PET.RWTC.W>    
[^3]: <https://insideevs.com/news/344007/monthly-plug-in-ev-sales-scorecard-historical-charts/>
