#include "kdot.h"
#include "nn.h"
#include "dt.h"


uint16_t xVal = 0;
uint16_t yVal = 0;
uint16_t zVal = 0;
bool calibrated = false;
static char* orientations[7] = {"up","down","forward","backward","left","right","undefined"};
uint8_t orientLutK[6] = {0, 0, 0, 0, 0, 0};


int checkOrientLut(){
  int differences = 0;
  for(int i = 0; i < 6; i++){
  for(int ii = 0; ii < 6; ii++){
    if(orientLutK[i] == orientLutK[ii])
      differences++;
  }}

  if(differences == 6*6-6)
    return 1;
  
  return 0;
}

void setup(){
  Serial.begin(9600);
  delay(20);
}


void loop(){
  if(!calibrated){
    for(int i = 0; i < 6; i++){
      Serial.print("set device in ");
      Serial.print(orientations[i]);
      Serial.println(" orientation");
      while(!Serial.available());
      while(Serial.available()){Serial.read();}
      xVal = analogRead(A0);
      yVal = analogRead(A1);
      zVal = analogRead(A2);
      orientLutK[closestPoint(xVal, yVal, zVal)] = i;
    }
    calibrated = true;
  }else{
    while(!Serial.available());
    char ori = Serial.read();
    delay(10);
    while(Serial.available()){Serial.read();}
    switch(ori){
      case 'u':
        ori = 0; break;
      case 'd':
        ori = 1; break;
      case 'l':
        ori = 4; break;
      case 'r':
        ori = 5; break;
      case 'f':
        ori = 2; break;
      case 'b':
        ori = 3; break;
      default:
        ori = 6;
    }
    xVal = analogRead(A0);
    yVal = analogRead(A1);
    zVal = analogRead(A2);
    Serial.print(orientations[ori]);
    Serial.print(" ");
    //k-means
    Serial.print(orientations[orientLutK[closestPoint(xVal, yVal, zVal)]]);
    Serial.print(" ");
    //neural network
    Serial.print(orientations[orientLutK[runNN(xVal, yVal, zVal)]]);
    Serial.print(" ");
    //decison tree
    Serial.println(orientations[runDT(xVal, yVal, zVal)]);
    delay(100);
  }
}
