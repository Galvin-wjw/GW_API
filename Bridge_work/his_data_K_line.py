# coding:utf-8
import requests
import json
import matplotlib.finance as mpf
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
import matplotlib

def send_requset():
    url = "https://trade.api.lwork.com/v1/chart"
    headers = {
        "Host":"trade.api.lwork.com",
        "content-type":"application/json",
        "x-api-tenantid": "T90000",
        "x-api-token": "BpUPBvRl4e3wiIOU",
        "x-api-serverid":'73',
    }

    params = {
                 "vendor": "mt4",
        "period": "d1",
        "from":"2017-08-01T00:00:01Z",
        "to":"2017-08-19T00:00:01Z",
        "symbol":"EURUSD"
    }

    response = requests.get(
        url = url,
        headers = headers,
        params = params
    )

    # print(response.url)
    # print(response.headers)
    #
    # print('Response HTTP Status Code: {status_code}'.format(
    #     status_code=response.status_code))
    # print('Response HTTP Response Body: {content}'.format(
    #     content=response.content))

    #print(response.text)
   # data_list = {}
    open = []
    close = []
    high = []
    low = []

    data_list = json.loads(response.text)
    data = data_list['data']
    #print(data)
    for i in range(len(data)):
        close.append(data[i]['close'])
        open.append(data[i]['open'])
        high.append(data[i]['high'])
        low.append(data[i]['low'])


    ax1 = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4, axisbg='w')
    plt.suptitle("subplot2grid")

    monthdays = matplotlib.dates.MonthLocator()
    mondays = WeekdayLocator(MONDAY)
    alldays = DayLocator()

    #设定日期的主次刻度
    ax1.xaxis.set_major_locator(mondays)
    ax1.xaxis.set_minor_locator(alldays)


    mondayFormatter = DateFormatter('%Y-%m-%d')  # 如：2-29-2015
    ax1.xaxis.set_major_formatter(mondayFormatter)

    ax1.xaxis_date()
    mpf.candlestick2_ohlc(ax1, open, high, low,
                          close, width=.75, colorup='r', colordown='g',alpha=0.75)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(90)

    #plt.grid(True)
    plt.show()


if __name__ == '__main__':
    send_requset()