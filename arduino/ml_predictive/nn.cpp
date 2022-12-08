#include "nn.h"

float inputs[3];
float outputs[6];

int runNN(float x, float y, float z){
	inputs[0] = x;
	inputs[1] = y;
	inputs[2] = z;

	//do first layer
	for(int i = 0; i < 6; i++){
		float tmp = 0.0;
		//dot product
		for(int ii = 0; ii < 3; ii++){
			tmp += inputs[ii] * nnWeights[ii][i];
		}
		outputs[i] = tmp;
	}
	//add bias
	for(int i = 0; i < 6; i++){
		outputs[i] += nnBiasses[i];
	} 
   
	//find highest number
	int rv = 0;
	for(int i = 0; i < 6; i++){
  		if(outputs[i] > outputs[rv])
			rv=i;
	}
	return rv;
}
