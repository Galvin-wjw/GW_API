# coding:utf-8

import websocket
import time
import sys

ONLINE_DOMAIN = "wss://trade.api.lwork.com/"
TENANTID = ""
TENANTTOKEN = ""

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("conn open")


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("invalid argv, expect TenantId, TenantToken")
    #     sys.exit()
    # if sys.argv[0] != 'demo.py':
    #     print("invalid argv, expect demo.py")
    #     sys.exit()
    TENANTID = "T001160"
    TENANTTOKEN = 'OlFO60EtEQiKHJz0'

    headers = {
        "x-api-tenantid": TENANTID,
        "x-api-token": TENANTTOKEN,
        "x-api-serverid":"63"
    }
   # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        ONLINE_DOMAIN + "/v1/quote/realtime/tick",
        header=headers,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
