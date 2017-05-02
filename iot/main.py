import time
import network
import urequests
from machine import ADC

from config import WLAN_NAME, WLAN_PASS, TOILET_URL, TOILET_ID, MIN_LDR_VAL, MAX_LDR_VAL


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting")
        sta_if.active(True)
        sta_if.connect(WLAN_NAME, WLAN_PASS)
        while not sta_if.isconnected():
            pass


def send_data(in_use):
    do_connect()
    r = urequests.post(TOILET_URL, json={"toilet": TOILET_ID, "in_use": in_use},
                       headers={'content-type': 'application/json'})
    r.close()


adc = ADC(0)
light_on = False

while True:
    print(adc.read())
    if adc.read() < MIN_LDR_VAL and light_on:
        light_on = False
        send_data(in_use=False)
    elif adc.read() > MAX_LDR_VAL and not light_on:
        light_on = True
        send_data(in_use=True)
    time.sleep(1)
