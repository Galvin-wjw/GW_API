# coding:utf-8
import requests
import json
import time
import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def send_requset():
    url = "https://trade.api.lwork.com/v1/chart"
    headers = {
        "Host":"trade.api.lwork.com",
        "content-type":"application/json",
        "x-api-tenantid": "T900002",
        "x-api-token": "BpUPBvRl4e3wiIOU",
        "x-api-serverid":'73',
    }

    params = {
        "vendor": "mt4",
        "period": "d1",
        "from":"2017-07-01T00:00:01Z",
        "to":"2017-09-01T00:00:01Z",
        "symbol":"EURUSD"
    }

    response = requests.get(
        url = url,
        headers = headers,
        params = params
    )
    return response

def moving_average(x, n):
    x = numpy.asarray(x) #Convert the input to an array.
    if type == 'simple':
        weights = numpy.ones(n) #Return a new array, filled with ones.
    else:
        weights = numpy.exp(numpy.linspace(-1., 0., n))#返回一个一维数组
    weights /= weights.sum()
    a = numpy.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    return a

if __name__ == '__main__':
    response = send_requset()
    #处理从接口获取的数据
    date = []
    close = []

    data_list = json.loads(response.text)
    data = data_list['data']
    format = '%m%d-%H:%M'  # 时间格式
    for i in range(len(data)):
        date.append(data[i]['timestamp'])
        close.append(data[i]['close'])
    for i in range(len(date)):
        # 经过localtime转换后变成struct_time
        date[i] = time.localtime(date[i])
        date[i] = time.strftime(format,date[i])

    fig, ax1 = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    plt.suptitle("EURUSD-Average-Line")
    #
    #设置横坐标
    x = numpy.arange(len(date))
    plt.xticks(x,date)
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(30))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)

    plt.grid(True)
    ma10 = moving_average(close, 10)
    ma20 = moving_average(close, 20)
    ma5 = moving_average(close, 5)

    ax1.plot(ma10, color='c', lw=1, label='MA (10)')
    ax1.plot(ma5, color='yellow', lw=1, label='MA (5)')
    ax1.plot(ma20, color='red', lw=1, label='MA (20)')
    plt.show()