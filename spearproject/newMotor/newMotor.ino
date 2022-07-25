/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial
Grupo de Automação e Robótica Aplicada/UFSM
V 1.2
 */

int incomingByte;

// Horizontal 

int dirX = 7;
int pulX = 6;
int enX = 5;

// Vertical

int dirY = 4;
int pulY = 3;
int enY = 2;

void passo(int pulPin, int dirPin, int speedM, bool movementDirection){
  digitalWrite(dirPin, movementDirection);
  delayMicroseconds(speedM);
  digitalWrite(pulPin, 1);
  delayMicroseconds(speedM);
  digitalWrite(pulPin, 0);
}
void setup(){
        Serial.begin(9600);
        pinMode(dirX, OUTPUT);
        pinMode(pulX, OUTPUT);
        pinMode(enX , OUTPUT);
        pinMode(dirY, OUTPUT);
        pinMode(pulY, OUTPUT);
        pinMode(enY , OUTPUT);
}

void loop(){
  Serial.flush();  
  incomingByte = Serial.read();

  // Eixo X
   
    if(incomingByte == 1){
      passo(pulX, dirX, 6000, 1);
    }
    if(incomingByte == 2){
      passo(pulX, dirX, 4000, 1); 
    }
    if(incomingByte == 3){
      passo(pulX, dirX, 3000, 1);
    }
    if(incomingByte == 4){
      passo(pulX, dirX, 2000, 1);
    }
    
    if(incomingByte == 5){
      passo(pulX, dirX, 6000, 0);
    }
    if(incomingByte == 6){
      passo(pulX, dirX, 4000, 0); 
    }
    if(incomingByte == 7){
      passo(pulX, dirX, 3000, 0);
    }
    if(incomingByte == 8){
      passo(pulX, dirX, 2000, 0);
    }

    // Eixo X
   
    if(incomingByte == 9){
      passo(pulY, dirY, 6000, 1);
    }
    if(incomingByte == 10){
      passo(pulY, dirY, 4000, 1); 
    }
    if(incomingByte == 11){
      passo(pulY, dirY, 3000, 1);
    }
    if(incomingByte == 12){
      passo(pulY, dirY, 2000, 1);
    }
    
    if(incomingByte == 13){
      passo(pulY, dirY, 6000, 0);
    }
    if(incomingByte == 14){
      passo(pulY, dirY, 4000, 0); 
    }
    if(incomingByte == 15){
      passo(pulY, dirY, 3000, 0);
    }
    if(incomingByte == 16){
      passo(pulY, dirY, 2000, 0);
    }

  }
  
  
