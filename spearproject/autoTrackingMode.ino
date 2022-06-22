/*
Algoritmo de movimentação dos motores baseado em visao computacional com comunicação serial

Grupo de Automação e Robótica Aplicada/UFSM

V 1.2
 */

byte incomingByte[2];

//Motor Grande / eixo horizontal

int dirX = 5;
int pulX = 6;
int enX = 7;

//Motor Pequeno / eixo vertical

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

if(incomingByte[0] == 3){  //EIXO X
  
  if(incomingByte[1] > 140){ //127 é o meio da camera mapeada de 0 a 255 com resolução de 640x480
                    digitalWrite(dirX, LOW);
                    delayMicroseconds(6000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(6000);
                    digitalWrite(pulX, LOW);  
  }
  if(incomingByte[1] < 115){
                    digitalWrite(dirX, HIGH);
                    delayMicroseconds(6000);
                    digitalWrite(pulX, HIGH);
                    delayMicroseconds(6000);
                    digitalWrite(pulX, LOW);                    
    }
  }
if(incomingByte[0] == 4){  //EIXO Y
  
  if(incomingByte[1] > 137){ //127 é o meio da camera mapeada de 0 a 255 com resolução de 640x480
                    digitalWrite(dirY, LOW);
                    delayMicroseconds(20);
                    digitalWrite(pulY, HIGH);
                    delayMicroseconds(20);
                    digitalWrite(pulY, LOW);
  }
  if(incomingByte[1] < 117){
                    digitalWrite(dirY, HIGH);
                    delayMicroseconds(20);
                    digitalWrite(pulY, HIGH);
                    delayMicroseconds(20);
                    digitalWrite(pulY, LOW); 
    }
  }
  
}
