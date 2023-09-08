# Dashboard 1: Cantonal COVID Statistics in Switzerland
Plotly and Django on GCP App Engine to illustrate cantonal COVID-19 statistics in Switzerland.  

I used Plotly library to create a graph of confirmed COVID-19 cases and deaths per canton in Switzerland after I pull data from an official source via its provided API. Afterwards, I simply added the link for this application in one of my public entries on my Django based web blog.  

Link to dashboard: https://dashboards.zeytinlik.ch/corona_stats_ch/

Output is something like below with a link to the official data source embedded in each canton label:  
  
![alt text](https://github.com/karakurto/dashboards/blob/main/Capture1.PNG?raw=true)

This graph uses 1 day old data because cantons upload their data at 18.00 during workdays. This also means that there will be fewer cantons in the graph if you generate a graph on Sundays or Mondays before 18.00.

You can learn more about application deployment to GCP App Engine here: https://github.com/karakurto/GCP-App-Engine-Standard

# Dashboard 2: Air Passenger Throughput in the US
BeautifulSoup to scrap data from a web page, pandas to create a DataFrame out of it and plotly to visualize US air passenger data. 

Data comes from TSA website since they do not provide this data in a programmatic way: https://www.tsa.gov/travel/passenger-volumes

Link to dashboard: https://dashboards.zeytinlik.ch/us-air-passengers/

Output is something like below with multiple traces to compare throughput across years. Idea of the dashboard is to give us an idea how air travel is recovering from the pandemic. This dashboard is interactive meaning you can select/unselect individual traces to compare certain years. When you hover over the traces, you can see the volume on specific days.
  
![alt text](https://github.com/karakurto/dashboards/blob/main/Capture2.PNG?raw=true)
