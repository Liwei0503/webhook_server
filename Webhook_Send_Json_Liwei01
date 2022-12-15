# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:09:25 2022

@author: Liwei
"""

import requests
import json
#webhook_url = 'https://webhook.site/fbca32a8-1303-4ba4-868c-db6ed772c5fc'
#webhook_url = '	https://webhook.site/76973b57-fb74-421c-9e21-16adc222b8c4'
#webhook_url = 'https://0a09-114-36-180-74.jp.ngrok.io/webhook'
#webhook_url = 'https://7e9e-114-36-180-74.jp.ngrok.io/webhook'
webhook_url = 'https://02ac-114-36-180-74.jp.ngrok.io/webhook'
#https://94ea-114-36-199-27.jp.ngrok.io
#https://94ea-114-36-199-27.jp.ngrok.io/
#data = { 'name': 'This is an example for webhook........................  TEST' }

#data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } 
data = {  "pair": "TQQQ", "side": "sell",  "size": "2",  "update_size": "1"}
#data = {  "pair": "TQQQ", "side": "buy",  "size": "2",  "update_size": "1"}

# data = {  "pair": "SQQQ", "side": "sell",  "size": "1",  "update_size": "1"}
#data = {  "pair": "SQQQ", "side": "buy",  "size": "1",  "update_size": "1"}

requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
#requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'text/plain'})
