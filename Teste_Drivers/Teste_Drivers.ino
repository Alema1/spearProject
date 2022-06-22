//Motor Grande 

int dirx = 7;
int pulx = 6;
int enx = 5;

//Motor Pequeno

int diry = 4;
int puly = 3;
int eny = 2;

void setup() {

  pinMode(dirx, OUTPUT);
  pinMode(pulx, OUTPUT);
  pinMode(enx, OUTPUT);
  pinMode(diry, OUTPUT);
  pinMode(puly, OUTPUT);
  pinMode(eny, OUTPUT);
  
}

void loop() {
  int i;
  for(i=0; i<1600; i++){
    digitalWrite(dirx, HIGH);
    digitalWrite(diry, HIGH);
    digitalWrite(puly, HIGH);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(pulx, HIGH);   // turn the LED on (HIGH is the voltage level)
    delayMicroseconds(10000);                       // wait for a second
    digitalWrite(puly, LOW);    // turn the LED off by making the voltage LOW
    digitalWrite(pulx, LOW);    // turn the LED off by making the voltage LOW
    delayMicroseconds(10000);
  }
   for(i=0; i<1600; i++){
    digitalWrite(diry, LOW);
    digitalWrite(diry, LOW);
    digitalWrite(puly, HIGH);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(pulx, HIGH);   // turn the LED on (HIGH is the voltage level)
    delayMicroseconds(10000);                       // wait for a second
    digitalWrite(puly, LOW);    // turn the LED off by making the voltage LOW
    digitalWrite(pulx, LOW);    // turn the LED off by making the voltage LOW
    delayMicroseconds(10000);
  }
}

/*
O limite do driver grande e de 16 microsengundos.
O limite do driver pequeno e de 4 microsegundos
*/
