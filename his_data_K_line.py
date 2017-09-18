# coding:utf-8
import requests
import json
import time
import numpy
import matplotlib.finance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def send_requset():
    url = "https://trade.api.lwork.com/v1/chart"
    headers = {
        "Host":"trade.api.lwork.com",
        "content-type":"application/json",
        "x-api-tenantid": "*****",
        "x-api-token": "****",
        "x-api-serverid":'****',
    }

    params = {
        "vendor": "mt4",
        "period": "d1",
        "from":"2017-08-01T00:00:01Z",
        "to":"2017-09-01T00:00:01Z",
        "symbol":"EURUSD"
    }

    response = requests.get(
        url = url,
        headers = headers,
        params = params
    )
    return response

if __name__ == '__main__':
    response = send_requset()
    #处理从接口获取的数据
    trade_time = []
    open = []
    close = []
    high = []
    low = []
    data_list = json.loads(response.text)
    data = data_list['data']
    format = '%m-%d-%H:%M'
    for i in range(len(data)):
        trade_time.append(data[i]['timestamp'])
        close.append(data[i]['close'])
        open.append(data[i]['open'])
        high.append(data[i]['high'])
        low.append(data[i]['low'])
    for i in range(len(trade_time)):
        trade_time[i] = time.localtime(trade_time[i])#经过localtime转换后变成time.struct_time
        trade_time[i] = time.strftime(format,trade_time[i])
    #print(trade_time)
    fig, ax1 = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    plt.suptitle("EURUSD-D1-K-line")

    #设置横坐标
    x = numpy.arange(len(trade_time))
    plt.xticks(x,trade_time)
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(9))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)

    #绘制K线图
    mpf.candlestick2_ohlc(ax1, open, high, low,
                          close, width=.75, colorup='r', colordown='g',alpha=1)

    plt.grid(True)
    plt.show()
