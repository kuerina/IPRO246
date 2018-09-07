/*
Created by Yvan / https://Brainy-Bits.com

This code is in the public domain...
You can: copy it, use it, modify it, share it or just plain ignore it!
Thx!

*/

// NRF24L01 Module Tutorial - Code for Transmitter using Arduino NANO

//Include needed Libraries at beginning
#include "nRF24L01.h" //NRF24L01 library created by TMRh20 https://github.com/TMRh20/RF24
#include "RF24.h"
#include "SPI.h"

#define SwitchPin 8 // Arcade switch is connected to Pin 8 on NANO


RF24 radio(9,10); // NRF24L01 used SPI pins + Pin 9 and 10 on the NANO
int sec;
void setup(void){
  pinMode(SwitchPin, INPUT_PULLUP); // Define the arcade switch NANO pin as an Input using Internal Pullups
  digitalWrite(SwitchPin,HIGH); // Set Pin to HIGH at beginning
  sec=0;
  radio.begin(); // Start the NRF24L01
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x72);
  radio.openWritingPipe(0xF0F0F0F0E1LL); // Get NRF24L01 ready to transmit
  radio.enableDynamicPayloads();
  radio.powerUp();
}

void loop(void){
  const char lineMes[]="hello world";
  radio.write(&lineMes, sizeof(lineMes)); // Send value through NRF24L01
  delay(1000);
  char lineMes2[]="hello Ufarm";
  radio.write(&lineMes2, sizeof(lineMes2)); // Send value through NRF24L01

}

