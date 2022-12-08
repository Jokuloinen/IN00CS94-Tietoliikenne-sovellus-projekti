#include "kdot.h"
#include "math.h"
#include <Arduino.h>
float distances[6];
void clearDistances(){
  for(int i = 0; i < 6; i++)
    distances[i] = 0;
}

int closestPoint(float x, float y, float z){
  clearDistances();
  //calculate distances
  for(int i = 0; i < 6; i++){
    distances[i] = sqrt(pow((x-kPoints[i][0]),2)+pow((y-kPoints[i][1]),2)+pow((z-kPoints[i][2]),2));
  }
  //find lowest distance
  int lIndex = 0;
  for(int i = 0; i < 6; i++){
    if(distances[lIndex] > distances[i]){
      lIndex = i;
    }
  }
  return lIndex;
}
