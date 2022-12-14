#include <math.h>
#include <RHReliableDatagram.h>
#include <RH_ASK.h>
const int XInPin = A0;
const int YInPin = A1;
const int ZInPin = A2;

//data from pin
uint16_t xVal = 0;
uint16_t yVal = 0;
uint16_t zVal = 0;

uint8_t message[8];//(16+16+16+8)/8
RH_ASK driver;//pins 11 and 12 for rx and tx
RHReliableDatagram rhd(driver, 53);

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  if (!rhd.init()){
    Serial.println("init failed");
  }
  delay(200);
}

char inputOrient;
int inputLoop = 0;
void loop() {
  driver.setModeTx();
  //wait for input
  Serial.println("give orientation and messurment");
  Serial.println("xyz + num");
  Serial.println("x5, y6");

  while(!Serial.available());
  inputOrient = Serial.read();
  //set the orient bit
  if((inputOrient < 'x') || (inputOrient > 'z')){//if invalid value given
    return;
  }
  Serial.println("how many mesurments");
  while(!Serial.available());
  inputLoop = Serial.parseInt(SKIP_NONE);

  for(inputLoop; inputLoop != 0; inputLoop--){
    // read the analog in value:
    xVal = analogRead(XInPin);
    yVal = analogRead(YInPin);
    zVal = analogRead(ZInPin);

    //kalibrointi
    /*ax = (((xVal - 261) / 133) * 19.62) - 9.81;
    ay = (((yVal - 261) / 133) * 19.62) - 9.81;
    az = (((zVal - 261) / 133) * 19.62) - 9.81;*/
 
    // print the results to the Serial Monitor:
    //Serial.print(millis());
    //Serial.print(" aika \t");
    Serial.print(xVal);
    Serial.print(", ");
    Serial.print(yVal);
    Serial.print(", ");
    Serial.println(zVal);

    //clear message
    for(int i=0; i<7; i++){message[i]=0;}
    //fill message
    message[0]=xVal >> 8;
    message[1]=xVal;
    message[2]=yVal >> 8;
    message[3]=yVal;
    message[4]=zVal >> 8;
    message[5]=zVal;
    message[6]=inputOrient;
    message[7]='\0';
    //send message
    rhd.sendtoWait(message, 8, 254);

    delay(100);
  }
  delay(200);
}
