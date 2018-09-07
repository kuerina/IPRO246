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
char SentMessage[] = {"hello World"}; // Used to store value before being sent through the NRF24L01


RF24 radio(9,10); // NRF24L01 used SPI pins + Pin 9 and 10 on the NANO

const uint64_t pipe = 0xE6E6E6E6E6E6; // Needs to be the same for communicating between 2 NRF24L01 

int sec;
void setup(void){

pinMode(SwitchPin, INPUT_PULLUP); // Define the arcade switch NANO pin as an Input using Internal Pullups
digitalWrite(SwitchPin,HIGH); // Set Pin to HIGH at beginning
sec=0;
radio.begin(); // Start the NRF24L01
radio.openWritingPipe(pipe); // Get NRF24L01 ready to transmit
}

void loop(void){
sec++;
 // If Switch is Activated
SentMessage = {"hello World"};
radio.write(SentMessage, 1); // Send value through NRF24L01
delay(1000);

SentMessage = {"hello Ufarm"};
radio.write(SentMessage, 1); // Send value through NRF24L01

}

