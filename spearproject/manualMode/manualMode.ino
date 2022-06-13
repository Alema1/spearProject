/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial

Grupo de Automação e Robótica Aplicada/UFSM

V 1.5
 */

byte incomingByte[3];

// Horizontal 

int dirX = 7;
int pulX = 6;
int enX = 5;

// Vertical

int dirY = 4;
int pulY = 3;
int enY = 2;

int MotorSpeed;
int indicatorX;
int convertedValueX;


void setup() {
        Serial.begin(19200);
        pinMode(dirX, OUTPUT);
        pinMode(pulX, OUTPUT);
        pinMode(enX , OUTPUT);
        pinMode(dirY, OUTPUT);
        pinMode(pulY, OUTPUT);
        pinMode(enY , OUTPUT);
}

void loop(){
  
Serial.readBytes(incomingByte,3);

if(incomingByte[0] == 1){  //EIXO X
  switch (incomingByte[1]){
    case 0:
    if(incomingByte[2]<128){
     digitalWrite(dirX, LOW);
     delayMicroseconds(3000);
     digitalWrite(pulX, HIGH);
     delayMicroseconds(3000);
     digitalWrite(pulX, LOW);
    }
    if(incomingByte[2]>128){
     digitalWrite(dirX, LOW);
     delayMicroseconds(2000);
     digitalWrite(pulX, HIGH);
     delayMicroseconds(2000);
     digitalWrite(pulX, LOW);
    }
    break;
    case 1:
    if(incomingByte[2]<128){
     digitalWrite(dirX, LOW);
     delayMicroseconds(5000);
     digitalWrite(pulX, HIGH);
     delayMicroseconds(5000);
     digitalWrite(pulX, LOW);
    }
    if(incomingByte[2]>128){
     digitalWrite(dirX, LOW);
     delayMicroseconds(4000);
     digitalWrite(pulX, HIGH);
     delayMicroseconds(4000);
     digitalWrite(pulX, LOW);
    }
    break;

    default:

    break;
  }
}
}
