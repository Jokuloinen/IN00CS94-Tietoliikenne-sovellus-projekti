/*void setup(){
  Serial.begin(9600); // sarjaportin nopeus
}
int number = 0;

void loop(){
  Serial.print("Numero on ");
  Serial.println(number);    // tulosta numero

  delay(500); // 0.5 s viive
  number++;
/*  
  int x = ;
  int y = ;
  int z = ;
*/

/*}*/
#include <math.h>
const int XInPin = A0;
const int YInPin = A1;
const int ZInPin = A2;

//data from pin
float xVal = 0;
float yVal = 0; 
float zVal = 0; 

//calculated from pin data with calibration
float ax= 0;
float ay= 0;
float az= 0;


/*const int kalibtab[3][3] = {
                        {394, 329, 261},//x  ylös  vaaka alas
                        {389, 306, 261},//y  
                        {269, 333, 394}//z   
                      };*/

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  delay(2000);
  Serial.print("ax,ay,az\n");
}

void loop() {
  // read the analog in value:
  xVal = analogRead(XInPin);
  yVal = analogRead(YInPin);
  zVal = analogRead(ZInPin);

  //kalibrointi
  //ax=map(xVal, 261, 394, -9.81, 9.81);//0.1493*xVal-66.5;
  //ax=(((ax-261)/(394-261))*19.62)-9.81;
  ax = (((xVal - 261) / 133) * 19.62) - 9.81;
  //ay=map(yVal, 261, 389, -9.81, 9.81);//0.1499*yVal-64;
  ay = (((yVal - 261) / 133) * 19.62) - 9.81;
  //az=map(zVal, 269, 394, -9.81, 9.81);// 0.1463*zVal-62.5;
  az = (((zVal - 261) / 133) * 19.62) - 9.81;
  //a=sqrt(ax*ax+ay*ay+az*az);

  //rajataan arvot
  ax = min(9.81, ax); ax = max(-9.81, ax);
  ay = min(9.81, ay); ay = max(-9.81, ay);
  az = min(9.81, az); az = max(-9.81, az);
 
  // print the results to the Serial Monitor:
  //Serial.print(millis());
  //Serial.print(" aika \t");
  Serial.print(ax);
  Serial.print(", ");
  Serial.print(ay);
  Serial.print(", ");
  Serial.println(az);

  delay(500);
}
