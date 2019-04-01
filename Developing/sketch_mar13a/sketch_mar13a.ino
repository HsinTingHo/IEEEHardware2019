int data; //python input
int trigPin = 11;//utrosonic sensor
int echoPin = 13;//utrosonic sensor
int motor1p = 8;
int motor1n = 9;
int motor2p = 10;
int motor2n = 11;
long distance;

long getDistance(int data, int trigPin, int echoPin){
  long duration, cm, inches;
  if(data == 48){//when input is 0, somehow arduino shows 48
     digitalWrite(trigPin, LOW);
     delayMicroseconds(5);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);

     pinMode(echoPin, INPUT);
     duration = pulseIn(echoPin, HIGH);

     //cm = (duration/2) / 29.1;
     inches = (duration/2) / 74;
  }
 
  return inches;
}

//return true when an object is within 3 inches
bool withinDistance(long d){
  long inches = 3;
  bool result;
    if(d < inches){
      result = true;
    }   
    else{
      result = false;
    }
    return result;
}


void move(char input){
  long runTime =millis();
  int endTime = 5000;
  //Serial.print(input);
  if (input=='forward')
  { 
    //runTime <= endTime
    while(runTime<endTime){
      Serial.print("forward");
      digitalWrite(motor1p, HIGH);
      digitalWrite(motor1n, LOW);
      digitalWrite(motor2p, HIGH);
      digitalWrite(motor2n, LOW);
      runTime ++;
    }

  }
  if (input=='right')
  { 
    //runTime <= endTime
    while(runTime<endTime){
      Serial.print("right");
      digitalWrite(motor1p, HIGH);
      digitalWrite(motor1n, LOW);
      digitalWrite(motor2p, LOW);
      digitalWrite(motor2n, HIGH);
      runTime ++;
    }

  }
  if (input=='backward')
  { 
    //runTime <= endTime
    while(runTime<endTime){
      Serial.print("backward");
      digitalWrite(motor1p, LOW);
      digitalWrite(motor1n, HIGH);
      digitalWrite(motor2p, LOW);
      digitalWrite(motor2n, HIGH);
      runTime ++;
    }

  }
  if (input=='left')
  { 
    //runTime <= endTime
    while(runTime<endTime){
      Serial.print("left");
      digitalWrite(motor1p, LOW);
      digitalWrite(motor1n, HIGH);
      digitalWrite(motor2p, HIGH);
      digitalWrite(motor2n, LOW);
      runTime ++;
    }

  }

}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  //motor
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
}

void loop() {
/*for connecting pi
  a++;                          // a value increase every loop
  sprintf(dataString,"%02X",a); // convert a value to hexa 
  Serial.println(dataString);   // send the data
  delay(1000);
  */
 
  /*
  while(Serial.available()){
    data = Serial.read(); //Get the input from python   
    distance = getDistance(data, trigPin, echoPin);
    Serial.print(distance);   
  }
  */
  move(Serial.read());
  delay(20);
  
  
}
