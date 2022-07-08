/*
Algoritmo de movimentação dos motores baseado em controle manual com joystick com comunicação serial

Grupo de Automação e Robótica Aplicada/UFSM

V 1.5
 */

char incomingByte;

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
	if(Serial.available() > 0){
		incomingByte = Serial.read();
	} 
  
	switch(incomingByte){
    // Eixo X centrado  
		case '0':
		break;
    // Eixo Y Esq
		case '1':
			passo(pulX, dirX, 6000, 1);
		break;
		case '2':
			passo(pulX, dirX, 4000, 1);
		break;
		case '3':
			passo(pulX, dirX, 3000, 1);
		break;
		case '4':
			passo(pulX, dirX, 2000, 1);
		break;
    // Eixo X Dir
		case '5':
			passo(pulX, dirX, 6000, 0);
		break;
		case '6':
			passo(pulX, dirX, 4000, 0);
		break;
		case '7':
			passo(pulX, dirX, 3000, 0);
		break;
		case '8':
			passo(pulX, dirX, 2000, 0);
		break;
    // Eixo Y Cima
    case '9':
      passo(pulY, dirY, 5000, 1);
    break;
    case 'a':
      passo(pulY, dirY, 4000, 1);
    break;
    case 'b':
      passo(pulY, dirY, 2000, 1);
    break;
    case 'c':
      passo(pulY, dirY, 700, 1);
    break;
        // Eixo Y Baixo
    case 'd':
      passo(pulY, dirY, 5000, 0);
    break;
    case 'e':
      passo(pulY, dirY, 4000, 0);
    break;
    case 'f':
      passo(pulY, dirY, 2000, 0);
    break;
    case 'g':
      passo(pulY, dirY, 700, 0);
    break;
	}
}
