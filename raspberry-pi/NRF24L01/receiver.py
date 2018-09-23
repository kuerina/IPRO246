#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Example program to receive packets from the radio link
#

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from lib_nrf24 import NRF24

import time
import spidev



pipes = [[0xe8, 0xe8, 0xf0, 0xf0, 0xe1], [0xf0, 0xf0, 0xf0, 0xf0, 0xe1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,11)

radio.setRetries(15,15)

radio.setPayloadSize(64)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

radio.printDetails()

radio.startListening()

c=1

while True:
   # akpl_buf = [c,1, 2, 3,4,5,6,7,8,9,0,1, 2, 3,4,5,6,7,8]
   # pipe = [0]
	while radio.available(0): #pipe):
      		time.sleep(1/100)
   	recv_buffer = []
   	radio.read(recv_buffer, radio.getDynamicPayloadSize())
   	string=""
	print("received: {}".format(recv_buffer))
	for n in recv_buffer:
		print(n)
		if(n>=32 and n<= 126):
			string += chr(n)
	print("{}".format(string))
		

#    if (len(recv_buffer)>10):
#	print("Received")
#	print(recv_buffer)
    #c = c + 1

    #if (c&1) == 0:
    #    radio2.writeAckPayload(1, akpl_buf, len(akpl_buf))
  #      print ("Loaded payload reply:"),
  #      print (akpl_buf)
    #else:
	
       # print ("(No return payload)")

