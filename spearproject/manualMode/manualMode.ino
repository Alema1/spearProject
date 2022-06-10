/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial

Grupo de Automação e Robótica Aplicada/UFSM

V 1.2
 */

byte incomingByte[2];

//Motor Grande 

int dirX = 7;
int pulX = 6;
int enX = 5;

//Motor Pequeno

int dirY = 4;
int pulY = 3;
int enY = 2;

int speedM;
int indicatorX;


void setup() {
  
        Serial.begin(19200);
        pinMode(dirX, OUTPUT);
        pinMode(pulX, OUTPUT);
        pinMode(enX, OUTPUT);
        pinMode(dirY, OUTPUT);
        pinMode(pulY, OUTPUT);
        pinMode(enY, OUTPUT);
}

void loop(){
  
Serial.readBytes(incomingByte,2);

if(incomingByte[0] == 1){  //EIXO X
  
  if(incomingByte[1] == 0){
                    indicatorX = 0; 
  }
  if(incomingByte[1] == 1){
                    indicatorX = 1;                   
  }
    if(incomingByte[1] == 2){
                    indicatorX = 2;                   
  }
    if(incomingByte[1] == 3){
                    indicatorX = 3;                   
  }
}
if(incomingByte[0] == 2){  //EIXO Y
  
  if(incomingByte[1] > 196){
    while(1){
                    digitalWrite(dirX, LOW);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, LOW);
    }
  }
  if(incomingByte[1] < 60){
                    digitalWrite(dirX, HIGH);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, LOW); 
    }
  }

    while(1){
                    digitalWrite(dirX, LOW);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(4000);
                    digitalWrite(pulX, LOW);
    }  
  
}
