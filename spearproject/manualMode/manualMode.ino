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

void setup() {
        Serial.begin(9600);
        pinMode(dirX, OUTPUT);
        pinMode(pulX, OUTPUT);
        pinMode(enX , OUTPUT);
        pinMode(dirY, OUTPUT);
        pinMode(pulY, OUTPUT);
        pinMode(enY , OUTPUT);
}

void passo(int pulPin, int dirPin, int speedM, bool movementDirection){
  digitalWrite(dirPin, movementDirection);
  delayMicroseconds(speedM);
  digitalWrite(pulPin, 1);
  delayMicroseconds(speedM);
  digitalWrite(pulPin, 0);
}

void loop(){
  digitalWrite(enX, 0); 
  Serial.readBytes(incomingByte,3);
  // O byte recebido eh assim: [xxx, xxx, xxx]
  // Primeiro byte eh o cabecalho, segundo eh o quadrante e terceiro valor
  if(incomingByte[0] == 1){  // Se for eixo X
    switch (incomingByte[1]){
      case 0: // Primeiro Quadrante
        if(incomingByte[2]<128){
          passo(pulX, dirX, 3000, 1);
        }
        else{
          passo(pulX, dirX, 2000, 1);
        }
      break;
      case 1: //Segundo Quadrante
        if(incomingByte[2]<128){
          passo(pulX, dirX, 5000, 1);
        }
        else{
          passo(pulX, dirX, 4000, 1);
        }
      break;
      case 2: // Terceito Quadrante, zero aqui eh o joystick centrado
        if((incomingByte[2]<128) && (incomingByte[2] != 0)){
          passo(pulX, dirX, 5000, 0);
        }
        if((incomingByte[2]>128) && (incomingByte[2] != 0)){
          passo(pulX, dirX, 4000, 0);
        }
      break;
      case 3: // Quarto Quadrante
        if(incomingByte[2]<128){
          passo(pulX, dirX, 3000, 0);
        }
        else{
          passo(pulX, dirX, 2000, 0);
        }
      break;
      default:
        //passo(pulX, dirX, 7000, 0);
      break;
    }
  }
}
