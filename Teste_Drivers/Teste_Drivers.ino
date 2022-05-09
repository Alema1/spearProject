//Motor Grande 

int dirx = 5;
int pulx = 6;
int enx = 7;

//Motor Pequeno

int diry = 10;
int puly = 8;
int eny = 9;

void setup() {

  pinMode(dirx, OUTPUT);
  pinMode(pulx, OUTPUT);
  pinMode(enx, OUTPUT);
  pinMode(diry, OUTPUT);
  pinMode(puly, OUTPUT);
  pinMode(eny, OUTPUT);
  
}

void loop() {

  while(delay(5000)){

    
  }
  
  digitalWrite(puly, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(pulx, HIGH);   // turn the LED on (HIGH is the voltage level)
  delayMicroseconds(10000);                       // wait for a second
  digitalWrite(puly, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(pulx, LOW);    // turn the LED off by making the voltage LOW
  delayMicroseconds(10000);                       // wait for a second
  
}

/*
O limite do driver grande e de 16 microsengundos.
O limite do driver pequeno e de 4 microsegundos
*/
