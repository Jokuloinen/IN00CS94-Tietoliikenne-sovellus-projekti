#include "dt.h"
int runDT(uint16_t x, uint16_t y, uint16_t z){
  int retval = 6;
  if((x+y+z) > 1000){//backward, right, down
    if(y>x){//backward, down
      if(z>y){//down
        retval = 1;
      }else{//backward
        retval = 3;
      }
    }else{//right
      retval = 5;
    }
  }else{//up, forward, left
    if(z>y){//forward left
      if(x>y){//forward
        retval = 2;
      }else{//left
        retval = 4;
      }
    }else{//up
      retval = 0;
    }
  }

  return retval;
}
