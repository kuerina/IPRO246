import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)
pipes=[[0xe7,0xe7,0xe7,0xe7,0xe7],[0xc2,0xc2,0xc2,0xc2,0xc2]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(10,6)
radio.setPayloadSize(32)
radio.setChannel(0x72)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1,pipes[1])
radio.printDetails()

radio.startListening()
t=True
while True:
      while not radio.available(0):
            time.sleep(1/100)
      receivedMessage = []
      radio.read(receivedMessage,radio.getDynamicPayloadSize())
      print("Received: {}".format(receivedMessage))
      print("Translating into unicode ...")
      string = ""
      for n in receivedMessage:
            if ( n >= 32 and n <= 126):
                  string += chr(n)
      print("Decoded Message: {}".format(string))
      t=False
