import time
import network
import urequests

from machine import ADC


TOILET_URL = "http://toilet.ngrok.io/toilet_lecture/"
TOILET_ID = 1
WLAN_NAME = 'APSL-Convidats'
WLAN_PASS = 'covagelada'
MIN_LDR_VAL = 100
MAX_LDR_VAL = 800


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting")
        sta_if.active(True)
        sta_if.connect(WLAN_NAME, WLAN_PASS)
        while not sta_if.isconnected():
            pass


def send_data(value):
    do_connect()
    r = urequests.post(TOILET_URL, json={"toilet": TOILET_ID, "value": value},
                       headers={'content-type': 'application/json'})
    r.close()


adc = ADC(0)
light_on = False

while True:
    print(adc.read())
    if adc.read() < MIN_LDR_VAL and light_on:
        light_on = False
        send_data("si")
    elif adc.read() > MAX_LDR_VAL and not light_on:
        light_on = True
        send_data("no")
    time.sleep(1)
