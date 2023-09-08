# https://medium.com/swlh/tsa-traveler-throughput-data-python-eeb39f658d71
# https://www.pauldesalvo.com/importing-and-analyzing-tsa-throughput-data-in-python/
# https://sparkbyexamples.com/pandas/conver-pandas-column-to-list/#:~:text=By%20using%20Series.values.tolist,the%20column%20values%20to%20list.
# https://stackoverflow.com/questions/67319777/using-a-list-for-x-and-y-axis-in-plotly
# https://cmdlinetips.com/2018/01/how-to-create-pandas-dataframe-from-multiple-lists/
# https://datagy.io/pandas-dataframe-from-list/
# https://plotly.com/python-api-reference/generated/plotly.express.line.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html
# https://community.plotly.com/t/how-to-plot-multiple-lines-on-the-same-y-axis-using-plotly-express/29219/13
# https://www.machinelearningplus.com/pandas/pandas-line-plot/
# https://www.codespeedy.com/how-to-change-figure-size-in-plotly-in-python/

import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
#import plotly.express as px

def passenger_volume():
    url = 'https://www.tsa.gov/coronavirus/passenger-throughput'
    req = requests.get(url)
    status_code = f"{req.status_code}"

    if status_code != "200":
        return url, status_code
        
    soup = BeautifulSoup(req.content, 'lxml')
    table = soup.find_all('table')[0]

    df = pd.read_html(str(table))[0]

    data_list = df.values.tolist()

    date, volume_2023, volume_2022, volume_2021, volume_2020, volume_2019 = [], [], [], [], [], []

    # We will have the data for trailing 364 dates starting from yesterday at the beginning of the list.
    for data in data_list:
      date.append(data[0])
      volume_2023.append(data[1])
      volume_2022.append(data[2])
      volume_2021.append(data[3])
      volume_2020.append(data[4])
      volume_2019.append(data[5])

    # To print the numbers from past to now. 
    date.reverse()
    volume_2023.reverse()
    volume_2022.reverse()
    volume_2021.reverse()
    volume_2020.reverse()
    volume_2019.reverse()

    # Data type in 2023 are floating numbers and volume of future dates are gieven as "nan". Therefore the modfication below.
    volume_2023 = [ 0 if str(i) == "nan" else int(i) for i in volume_2023]

    volume_diff_2023_2019 = [ volume_2023[i] - volume_2019[i] if volume_2023[i] != 0 else 0 for i in range(len(volume_2023)) ]

    df = pd.DataFrame({
      "date": date,
      "volume_2023": volume_2023,
      "volume_2022": volume_2022,
      "volume_2021": volume_2021,
      "volume_2020": volume_2020,
      "volume_2019": volume_2019,
      })

    #print(len(volume_2019))
    #print(len(volume_2020))
    #print(len(volume_2021))
    #print(len(volume_2022))
    #print(len(volume_2023))
    #print(len(date))
    #print(len(volume_diff_2023_2019))
    #print(df)
    #fig = px.line(df, x='date', y=['volume_2023','volume_2022', 'volume_2021', 'volume_2020', 'volume_2019', 'volume_diff_2023_2019']) 
    #fig.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=date, y=volume_2023,
        mode='lines',
        name="2023",
        line=dict(width=0.5, color='rgb(0, 153, 0)'),
    ))
    fig.add_trace(go.Scatter(
        x=date, y=volume_2022,
        mode='lines',
        name="2022",
        line=dict(width=0.5, color='rgb(255, 255, 0)'),
        visible='legendonly',
    ))
    fig.add_trace(go.Scatter(
        x=date, y=volume_2021,
        mode='lines',
        name="2021",
        line=dict(width=0.5, color='rgb(45, 45, 0)'),
        visible='legendonly',
    ))
    fig.add_trace(go.Scatter(
        x=date, y=volume_2020,
        mode='lines',
        name="2020",
        line=dict(width=0.5, color='rgb(255, 128, 45)'),
        visible='legendonly',
    ))
    fig.add_trace(go.Scatter(
        x=date, y=volume_2019,
        name="2019",
        line=dict(width=0.5, color='rgb(51, 0, 0)'),
    ))
    fig.add_trace(go.Scatter(
        x=date, y=volume_diff_2023_2019,
        mode='lines',
        name="2023 minus 2022",
        line=dict(width=0.5, color='rgb(255, 0, 0)'),
        visible='legendonly',
    ))

    fig.update_layout(
        title="US Air Passengers from 2019 to 2023 (Click on traces in the legend below to select/unselect and compare them)",
        xaxis_title="Trailing 364 Days",
        yaxis_title="Passenger Volume",
        paper_bgcolor="LightSteelBlue",
        yaxis=dict(
            titlefont=dict(size=20)),
        xaxis=dict(
            titlefont=dict(size=20)),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1,
            xanchor="left",
            x=0.35),
    )

    #fig.show()
    return fig.write_html("/tmp/us-air-passengers.html"), status_code



