import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)
pipes=[[0x37,0x

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,6)
radio.setPayloadSize(32)
radio.setChannel(0x72)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()
radio.openReadingPipe(1,pipes)
radio.printDetails()

radio.startListening()
t=True
while True:
   ackPL=[1]
   while not radio.available(0):
      time.sleep(1/100.)
   receivedMessage = []
   radio.read(receivedMessage,radio.getDynamicPayloadSize())
   print("Received: {}".format(receivedMessage))
   print("Translating into unicode ...")
   string = ""
   for n in receivedMessage:
   # decode
      if ( n >= 32 and n <= 126):
         string += chr(n)
   print(string)
   radio.writeAckPayload(1,ackPL,len(ackPL))
   print("Loaded payload reply of {}".format(ackPL))
   t=False
