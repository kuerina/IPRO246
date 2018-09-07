import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)
pipes = [[0xe6,0xe6,0xe6,0xe6,0xe6,0xe6]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,17)
radio.setPayloadSize(32)
radio.setChannel(0x60)
radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enabledDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1,pipes[1])
radio.printDetails()

radio.startListening()

while True:
	ackPL=[1]
	while not radio.available(0):
		time.sleep(1/100)
	receivedMessage = []
	radio.read(receivedMessage,radio.getDynamicPayloadSize())
	print("Received: {}".format(receivedMessage))
	print("Translating into unicode ...")
	string = ""
	for n in receivedMessage:
		# decode
		if (n>=32 and n <= 126):
			string += chr(n)
	print(string)
	radio.writeAckPayload(1,ackPL,len(ackPL))
	print("Loaded payload reply of {}".format(ackPL))
