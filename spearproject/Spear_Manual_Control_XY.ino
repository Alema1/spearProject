/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial

Grupo de Automação e Robótica Aplicada/UFSM

V 1.2
 */

byte incomingByte[2];

//Motor Grande 

int dirX = 5;
int pulX = 6;
int enX = 7;

//Motor Pequeno

int dirY = 10;
int pulY = 8;
int enY = 9;  


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
  
  if(incomingByte[1] > 196){
                    digitalWrite(dirX, LOW);
                    delayMicroseconds(5000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(5000);
                    digitalWrite(pulX, LOW);
                    Serial.flush();  
  }
  if(incomingByte[1] < 60){
                    digitalWrite(dirX, HIGH);
                    delayMicroseconds(5000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(5000);
                    digitalWrite(pulX, LOW);
                    Serial.flush();                     
    }
  }
if(incomingByte[0] == 2){  //EIXO Y
  
  if(incomingByte[1] > 196){
                    digitalWrite(dirY, LOW);
                    delayMicroseconds(10);
                    digitalWrite(pulY, HIGH);
                    delayMicroseconds(10);
                    digitalWrite(pulY, LOW);
  }
  if(incomingByte[1] < 60){
                    digitalWrite(dirY, HIGH);
                    delayMicroseconds(10);
                    digitalWrite(pulY, HIGH);
                    delayMicroseconds(10);
                    digitalWrite(pulY, LOW); 
    }
  }
  
}
