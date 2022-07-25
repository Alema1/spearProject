/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial
Grupo de Automação e Robótica Aplicada/UFSM
V 1.2
 */

byte incomingByte[2];

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
  Serial.readBytes(incomingByte,2);
  
  if(incomingByte[0] == 1){  //EIXO X 
    if(incomingByte[1] > 128){
      passo(pulX, dirX, 6000, 0);
    }
    if(incomingByte[1] > 159 and incomingByte[1] < 191){
      passo(pulX, dirX, 4000, 0); 
    }
    if(incomingByte[1] > 191 and incomingByte[1] < 223){
      passo(pulX, dirX, 3000, 0);
    }
    if(incomingByte[1] > 223 and incomingByte[1] < 255){
      passo(pulX, dirX, 2000, 1);                  
      }
    }
    
  if(incomingByte[0] == 2){  //EIXO Y
    if(incomingByte[1] > 196){
      passo(pulY, dirY, 1000, 1);
    }
    if(incomingByte[1] < 60){
      passo(pulY, dirY, 1000, 0);
    }
    Serial.flush();  
  }
  
}
