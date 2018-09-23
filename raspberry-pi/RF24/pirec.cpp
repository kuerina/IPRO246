#include <iostream>
#include "RF24.h"
using namespace std;
uint32_t pinCE = 25;
// "/dev/spidev0.0"
RF24 radio( 250000 , 25);
void setup(void)
{
	radio.begin();
	radio.enableDynamicPayloads();
	radio.setAutoAck(1);
	radio.setRetries(15,15);
	radio.setDataRate(RF24_1MBPS);
	radio.setPALevel(RF24_PA_MAX);
	radio.setChannel(76);
	radio.setCRCLength(RF24_CRC_16);
	radio.openReadingPipe(1,0xF0F0F0F0E1LL);
	radio.startListening();
}
void loop(void)
{
	char receivePayload[64];
	while (radio.available(0))
	{
		uint8_t len =radio.getDynamicPayloadSize();
		radio.read(receivePayload,len);
		cout << receivePayload << endl;
	}
}
int main(int argc, char** argv)
{
	setup();
	while(1)
		loop();
	return 0;
}
