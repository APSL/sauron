# -*- coding: utf-8 -*-
import urequests
import network

TOILET_URL = "http://toilet.ngrok.io/toilet_lecture/"
WLAN_NAME = 'APSL-Convidats'
WLAN_PASS = 'covagelada'


def connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WLAN_NAME,  WLAN_PASS)


urequests.post(TOILET_URL, json={"toilet": 1, "value": "si"}, headers={'content-type': 'application/json'})
