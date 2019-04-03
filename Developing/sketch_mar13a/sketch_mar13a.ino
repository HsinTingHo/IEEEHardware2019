int data; //python input

int motor1p = 8;
int motor1n = 9;
int motor2p = 10;
int motor2n = 11;
int pwm1 = 5;
int pwm2 = 6;

void move(int input){
  long runTime =millis();
  int endTime = runTime +10;
  int speed;
  int tempSpeed = 100; //full speed
  delay(200);
  Serial.print("  ");
  Serial.print(input);
  Serial.print("  ");
  if (input== 49)
  { 
    speed = map(tempSpeed/4, 0, 100, 0, 255);
    Serial.print("Speed");
    Serial.print(speed);
    endTime = runTime +50;
    while(runTime<endTime){
      Serial.print("forward");
      digitalWrite(motor1p, HIGH);
      digitalWrite(motor1n, LOW);
      digitalWrite(motor2p, HIGH);
      digitalWrite(motor2n, LOW);
      analogWrite(pwm1, speed);
      analogWrite(pwm2, speed);
      runTime ++;

    }
    delay(200);



  }
  if (input== 50)
  { 

    speed = map(tempSpeed/5, 0, 100, 0, 255);
    endTime = runTime +70;
    while(runTime<endTime){
      Serial.print("right");
      digitalWrite(motor1p, LOW);
      digitalWrite(motor1n, HIGH);
      digitalWrite(motor2p, HIGH);
      digitalWrite(motor2n, LOW);
      analogWrite(pwm1, speed);
      analogWrite(pwm2, speed);
      runTime ++;
      
    }
    


  }
  if (input== 51)
  { 
    //runTime <= endTime
    speed = map(tempSpeed/4, 0, 100, 0, 255);
    while(runTime<endTime){
      Serial.print("backward");
      digitalWrite(motor1p, LOW);
      digitalWrite(motor1n, HIGH);
      digitalWrite(motor2p, LOW);
      digitalWrite(motor2n, HIGH);
      analogWrite(pwm1, speed);
      analogWrite(pwm2, speed);
      runTime ++;
    }
    delay(200);

  }
  if (input== 52)
  { 
    //runTime <= endTime
    speed = map(tempSpeed/5, 0, 100, 0, 255);
    endTime = runTime +70;
    while(runTime<endTime){
      Serial.print("left");

      digitalWrite(motor1p, HIGH);
      digitalWrite(motor1n, LOW);
      digitalWrite(motor2p, LOW);
      digitalWrite(motor2n, HIGH);
      analogWrite(pwm1, speed);
      analogWrite(pwm2, speed);
      runTime ++;
    }

    
    delay(200);

  }

}

void stop(){
  Serial.print("Halt!!!");
  digitalWrite(motor1p, LOW);
  digitalWrite(motor1n, LOW);
  digitalWrite(motor2p, LOW);
  digitalWrite(motor2n, LOW);
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pwm1, OUTPUT);
  pinMode(pwm2, OUTPUT);

  //motor
  pinMode(motor1p, OUTPUT);
  pinMode(motor1n, OUTPUT);
  pinMode(motor2p, OUTPUT);
  pinMode(motor2n, OUTPUT);

  digitalWrite(motor1p, LOW);
  digitalWrite(motor1n, LOW);
  digitalWrite(motor2p, LOW);
  digitalWrite(motor2n, LOW);
}

void loop() {

  int input = Serial.read();
  
  move(49); //forward
  delay(1000);
  move(50); //right
  delay(400);
  move(49);
 // delay(400);
  //move(52); //left
  delay(200);
  //move(51); //back
  
  stop();
  delay(10000);
  
  
}
